import os
from dotenv import load_dotenv
from tronpy import Tron
from tronpy.providers import HTTPProvider

load_dotenv()

API_KEY = os.getenv("TRON_API_KEY")
client = Tron(provider=HTTPProvider(api_key=API_KEY))

def get_wallet_info(address: str) -> dict:
    try:
        account = client.get_account(address)
        resources = client.get_account_resource(address)
        balance = client.get_account_balance(address)

        if "NetUsed" in resources and "NetLimit" in resources:
            bandwidth = int(resources["NetLimit"] - resources["NetUsed"])
        elif "freeNetUsed" in resources and "freeNetLimit" in resources:
            bandwidth = int(resources["freeNetLimit"] - resources["freeNetUsed"])
        else:
            bandwidth = 0

        energy = int(resources.get("EnergyLimit", 0) - resources.get("EnergyUsed", 0))

        return {
            "bandwidth": bandwidth,
            "energy": energy,
            "balance": str(balance),
        }
    except Exception as e:
        raise ValueError(f"Error in get_wallet_info: {str(e)}")
