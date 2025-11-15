from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "API is working"}

import re
from fastapi import FastAPI

app= FastAPI()
@app.get("/validate-pan")
def validate_pan(pan: str):
    pan = pan.upper() #Fix: Handle lowercase PAN inputs
    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

    if re.match(pattern, pan):
        return {"pan": pan, "valid": True}
    else:
        return {"pan": pan, "valid": False}


