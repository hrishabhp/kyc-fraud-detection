def test_valid_aadhaar(api_client):
    response = api_client.get("/validate-aadhaar?aadhaar=987654321012")
    assert response.status_code == 200
    assert response.json()["result"] is True


def test_invalid_aadhaar(api_client):
    response = api_client.get("/validate-aadhaar?aadhaar=123456789")
    assert response.status_code == 200
    assert response.json()["result"] is False
