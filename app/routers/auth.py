from fastapi import APIRouter

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.get("/ping")
async def ping():
    return {"status": "auth-router ok"}
