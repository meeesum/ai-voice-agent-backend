from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.config import settings
import httpx
from pydantic import BaseModel


router = APIRouter(prefix="/api/auth", tags=["auth"])


class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(req: LoginRequest):
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(
            f"{settings.SUPABASE_URL}/auth/v1/token?grant_type=password",
            headers={
                "apikey": settings.SUPABASE_ANON_KEY,
                "Content-Type": "application/json",
            },
            json={
                "email": req.email,
                "password": req.password,
            },
        )
    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return resp.json()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Exchange email + password for Supabase JWT.
    This works with Swagger UI 'Authorize' button.
    """
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(
            f"{settings.SUPABASE_URL}/auth/v1/token?grant_type=password",
            headers={"apikey": settings.SUPABASE_ANON_KEY,
                     "Content-Type": "application/json"},
            json={"email": form_data.username, "password": form_data.password},
        )

    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    data = resp.json()
    return {"access_token": data["access_token"], "token_type": "bearer"}