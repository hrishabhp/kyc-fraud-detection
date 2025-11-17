from ..utils.helpers import get

def test_valid_pan():
    response = get("/validate-pan?pan=ABCDE1234F")
    assert response.status_code == 200
    assert response.json()["valid"] is True

def test_invalid_pan():
    response = get("/validate-pan?pan=12345")
    assert response.status_code == 200
    assert response.json()["valid"] is False
