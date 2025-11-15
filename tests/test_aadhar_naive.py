from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_naive_aadhar_rejects_invalid_by_checksum():
    # This a 12 digit number that should be invalid under Verhoeff checksum.

    bad_aadhar = "111111111111"
    resp = client.get("/validate-aadhar", params={"aadhar": bad_aadhar})
    assert resp.status_code == 200
    # A correct validator should mark it invalid (False)
    assert resp.json().get("valid") is False, f"Naive validator incorrectly accepted {bad_aadhar}"
