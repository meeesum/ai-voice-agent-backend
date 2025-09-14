# app/routers/calls.py
from fastapi import APIRouter, Depends, HTTPException
from ..dependencies.supabase_auth import get_current_user
from ..db.session import DBSession
from ..schemas.call import CallCreate, CallRead
import uuid

router = APIRouter(prefix="/api/calls", tags=["calls"])

@router.post("/", response_model=CallRead)
def create_call(call: CallCreate, user=Depends(get_current_user)):
    """
    Create a new call record.
    """
    with DBSession() as cur:
        call_id = uuid.uuid4()
        cur.execute(
            """
            INSERT INTO calls (id, driver_name, driver_phone, load_number)
            VALUES (%s, %s, %s, %s)
            RETURNING id, driver_name, driver_phone, load_number, outcome, transcript, summary, created_at;
            """,
            (call_id, call.driver_name, call.driver_phone, call.load_number)
        )
        result = cur.fetchone()
        if not result:
            raise HTTPException(status_code=500, detail="Failed to create call")
        return result

@router.get("/", response_model=list[CallRead])
def list_calls(user=Depends(get_current_user)):
    """
    List all calls.
    """
    with DBSession() as cur:
        cur.execute("SELECT * FROM calls ORDER BY created_at DESC;")
        return cur.fetchall()
