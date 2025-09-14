from fastapi import APIRouter, Depends
from ..dependencies.supabase_auth import get_current_user

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.get("/ping")
async def ping():
    return {"status": "auth-router ok"}

@router.get("/me")
async def me(user = Depends(get_current_user)):
    return {"user": user}
