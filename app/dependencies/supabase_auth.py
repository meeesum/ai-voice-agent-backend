from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ..config import settings
import httpx

# OAuth2PasswordBearer extracts "Authorization: Bearer <token>"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Verify a Supabase-issued JWT by calling Supabase's /auth/v1/user endpoint.
    Returns user payload if valid, else raises 401.
    """
    if not token:
        raise HTTPException(status_code=401, detail="Missing authentication token")

    headers = {
        "Authorization": f"Bearer {token}",
        "apikey": settings.SUPABASE_SERVICE_KEY,
    }
    url = f"{settings.SUPABASE_URL.rstrip('/')}/auth/v1/user"

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(url, headers=headers)

    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return resp.json()  # contains user id, email, role, etc.
