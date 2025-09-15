# services/retell_client.py
import httpx
import os

RETELL_API_URL = "https://api.retellai.com/v2/create-phone-call"
RETELL_API_KEY = os.getenv("RETELL_API_KEY")  # set in your environment

async def trigger_call(driver_name, driver_phone, load_number):
    payload = {
        "from_number": "+14157774444",  # your Retell number
        "to_number": driver_phone,      # call destination
        "override_agent_id": "your_agent_id",
        "override_agent_version": 1,
        "metadata": {"load_number": load_number},
        "retell_llm_dynamic_variables": {"driver_name": driver_name},
        "custom_sip_headers": {}
    }

    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(RETELL_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # will raise HTTPException if status != 2xx
        return response.json()
