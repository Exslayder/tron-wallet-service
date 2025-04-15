from pydantic import BaseModel, Field

class WalletRequestCreate(BaseModel):
    address: str = Field(..., example="Write TRX adress")

class WalletRequestOut(BaseModel):
    id: int
    address: str
    bandwidth: int
    energy: int
    balance: str

    class ConfigDict:
        from_attributes = True
