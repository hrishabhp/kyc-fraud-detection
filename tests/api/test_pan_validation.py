def test_valid_pan(api_client):
    response = api_client.get("/validate-pan?pan=ABCDE1234F")
    assert response.status_code == 200
    assert response.json()["result"] is True


def test_invalid_pan(api_client):
    response = api_client.get("/validate-pan?pan=12345")
    assert response.status_code == 200
    assert response.json()["result"] is False

