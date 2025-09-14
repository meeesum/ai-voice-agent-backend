import httpx
from app.config import settings

RETELL_API_URL = "https://api.retell.ai/call" 

async def trigger_call(driver_name: str, driver_phone: str, load_number: str):
    payload = {
        "driver_name": driver_name,
        "driver_phone": driver_phone,
        "load_number": load_number,
        "workspace_id": settings.RETELL_WORKSPACE_ID
    }
    headers = {"Authorization": f"Bearer {settings.RETELL_API_KEY}"}

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(RETELL_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()