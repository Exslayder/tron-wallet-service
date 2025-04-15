import pytest
from app.models import WalletRequest
from app.schemas import WalletRequestCreate
from app.database import SessionLocal

@pytest.mark.asyncio
async def test_wallet_creation():
    wallet_data = WalletRequestCreate(address="test")

    db = SessionLocal()

    api_response = {
        "bandwidth": 1000,
        "energy": 500,
        "balance": "123.45"
    }

    new_wallet = WalletRequest(
        address=wallet_data.address,
        bandwidth=api_response["bandwidth"],
        energy=api_response["energy"],
        balance=api_response["balance"]
    )
    db.add(new_wallet)
    await db.commit()
    await db.refresh(new_wallet)

    assert new_wallet.address == wallet_data.address
    assert new_wallet.bandwidth == api_response["bandwidth"]
    assert new_wallet.energy == api_response["energy"]
    assert new_wallet.balance == api_response["balance"]

    await db.close()