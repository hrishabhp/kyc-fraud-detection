import re
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.database import logs_collection

from pydantic import BaseModel
app = FastAPI()

class KYCRequest(BaseModel):
    type: str
    value: str
@app.get("/health")
def health():
    return {"status": "API is working"}

@app.get("/validate-pan")
async def validate_pan(pan: str):
    pan = pan.upper()  # Handle lowercase inputs
    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

    # PAN validation
    if re.match(pattern, pan):
        is_valid = True
        response = {"pan": pan, "valid": True}
    else:
        is_valid = False
        response = {"pan": pan, "valid": False}

    # Log into MongoDB
    await logs_collection.insert_one({
        "type": "PAN",
        "input": pan,
        "result": is_valid
    })

    return response

# Verhoeff algorithm tables
d_table = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,2,3,4,0,6,7,8,9,5],
    [2,3,4,0,1,7,8,9,5,6],
    [3,4,0,1,2,8,9,5,6,7],
    [4,0,1,2,3,9,5,6,7,8],
    [5,9,8,7,6,0,4,3,2,1],
    [6,5,9,8,7,1,0,4,3,2],
    [7,6,5,9,8,2,1,0,4,3],
    [8,7,6,5,9,3,2,1,0,4],
    [9,8,7,6,5,4,3,2,1,0]
]

p_table = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
]

inv_table = [0,4,3,2,1,5,6,7,8,9]

def verhoeff_check(number: str) -> bool:
    c = 0
    reversed_digits = map(int, reversed(number))

    for i, digit in enumerate(reversed_digits):
        c = d_table[c][p_table[(i % 8)][digit]]

    return c == 0

@app.get("/validate-aadhaar")
async def validate_aadhaar(aadhaar: str):
    # Basic checks
    if len(aadhaar) != 12 or not aadhaar.isdigit():
        is_valid = False
        response = {"aadhaar": aadhaar, "valid": False}
    else:
        # Check using Verhoeff algorithm
        if verhoeff_check(aadhaar):
            is_valid = True
            response = {"aadhaar": aadhaar, "valid": True}
        else:
            is_valid = False
            response = {"aadhaar": aadhaar, "valid": False}

    # Log into MongoDB
    await logs_collection.insert_one({
        "type": "AADHAAR",
        "input": aadhaar,
        "result": is_valid
    })

    return response
@app.post("/validate")
async def validate_kyc(data: KYCRequest):
    kyc_type = data.type.upper()
    value = data.value.strip()

    # -------------------- PAN VALIDATION --------------------
    if kyc_type == "PAN":
        # PAN Pattern
        pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

        if re.match(pattern, value.upper()):
            result = True
        else:
            result = False

        # Log PAN
        await logs_collection.insert_one({
            "type": "PAN",
            "input": value,
            "result": result
        })

        return {"type": "PAN", "value": value, "valid": result}

    # -------------------- AADHAAR VALIDATION --------------------
    elif kyc_type == "AADHAAR":

        if len(value) == 12 and value.isdigit() and verhoeff_check(value):
            result = True
        else:
            result = False

        # Log Aadhaar
        await logs_collection.insert_one({
            "type": "AADHAAR",
            "input": value,
            "result": result
        })

        return {"type": "AADHAAR", "value": value, "valid": result}

    # -------------------- INVALID TYPE --------------------
    else:
        return {"error": "Invalid type. Use PAN or AADHAAR"}

@app.get("/logs")
async def get_logs():
    cursor = logs_collection.find().sort("_id", -1).limit(20)
    logs = []
    async for document in cursor:
        document["_id"] = str(document["_id"])
        logs.append(document)
    return {"logs": logs}
@app.get("/stats")
async def get_stats():
    # PAN stats
    pan_valid = await logs_collection.count_documents({"type": "PAN", "result": True})
    pan_invalid = await logs_collection.count_documents({"type": "PAN", "result": False})

    # Aadhaar stats
    aadhaar_valid = await logs_collection.count_documents({"type": "AADHAAR", "result": True})
    aadhaar_invalid = await logs_collection.count_documents({"type": "AADHAAR", "result": False})

    # Total requests
    total_requests = await logs_collection.count_documents({})

    return {
        "total_requests": total_requests,
        "pan": {
            "valid": pan_valid,
            "invalid": pan_invalid
        },
        "aadhaar": {
            "valid": aadhaar_valid,
            "invalid": aadhaar_invalid
        }
    }
