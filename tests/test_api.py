from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_and_get_wallet():
    address = "TFTWNgDBkQ5wQoP8RXpRznnHvAVV8x5jLu" # Адрес реального аккаунта для проверки

    response = client.post("/wallet", json={"address": address})
    assert response.status_code == 200
    data = response.json()
    assert "bandwidth" in data
    assert "energy" in data
    assert "balance" in data

    get_response = client.get("/wallets")
    assert get_response.status_code == 200
    assert isinstance(get_response.json(), list)
