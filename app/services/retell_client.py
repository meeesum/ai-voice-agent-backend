import httpx
from ..config import settings

RETELL_API_URL = "https://api.retell.ai/call"

def trigger_call(driver_name: str, driver_phone: str, load_number: str):
    payload = {
        "driver_name": driver_name,
        "driver_phone": driver_phone,
        "load_number": load_number
    }
    headers = {"Authorization": f"Bearer {settings.RETELL_API_KEY}"}

    response = httpx.post(RETELL_API_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()
