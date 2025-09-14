from fastapi import APIRouter, Depends
from ..dependencies.supabase_auth import get_current_user

router = APIRouter(prefix="/api/calls", tags=["calls"])

@router.get("/")
async def list_calls(user = Depends(get_current_user)):
    # only authenticated users reach here
    return {"calls": [], "user": user}
