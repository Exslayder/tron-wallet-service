from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from . import models, schemas, tron_client
from .database import get_db

router = APIRouter()

@router.post("/wallet", response_model=schemas.WalletRequestOut)
async def fetch_wallet_data(request: schemas.WalletRequestCreate, db: AsyncSession = Depends(get_db)):
    try:
        data = tron_client.get_wallet_info(request.address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    new_entry = models.WalletRequest(
        address=request.address,
        bandwidth=data["bandwidth"],
        energy=data["energy"],
        balance=data["balance"]
    )
    db.add(new_entry)
    await db.commit()
    await db.refresh(new_entry)
    return new_entry

@router.get("/wallets", response_model=List[schemas.WalletRequestOut])
async def get_wallets(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.WalletRequest).offset(skip).limit(limit))
    return result.scalars().all()
