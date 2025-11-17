from ..utils.helpers import get

def test_valid_aadhaar():
    response = get("/validate-aadhaar?aadhaar=987654321012")
    assert response.status_code == 200
    assert response.json()["valid"] is True

def test_invalid_aadhaar():
    response = get("/validate-aadhaar?aadhaar=123456789")
    assert response.status_code == 200
    assert response.json()["valid"] is False

