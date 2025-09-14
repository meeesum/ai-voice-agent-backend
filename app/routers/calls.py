# app/routers/calls.py
from fastapi import APIRouter, Depends, HTTPException, Request
from ..dependencies.supabase_auth import get_current_user
from ..db.session import DBSession
from ..schemas.call import CallCreate, CallRead
from ..services.retell_client import trigger_call
from ..services.openai_client import generate_summary
import uuid

router = APIRouter(prefix="/api/calls", tags=["calls"])

@router.post("/", response_model=CallRead)
async def create_call(call: CallCreate, user=Depends(get_current_user)):
    with DBSession() as cur:
        call_id = uuid.uuid4()
        cur.execute(
            """
            INSERT INTO calls (id, driver_name, driver_phone, load_number)
            VALUES (%s, %s, %s, %s)
            RETURNING id, driver_name, driver_phone, load_number, outcome, transcript, summary, created_at;
            """,
            (call_id, call.driver_name, call.driver_phone, call.load_number),
        )
        result = cur.fetchone()

    try:
        await trigger_call(call.driver_name, call.driver_phone, call.load_number)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to trigger Retell: {e}")

    return result


@router.get("/", response_model=list[CallRead])
def list_calls(user=Depends(get_current_user)):
    with DBSession() as cur:
        cur.execute("SELECT * FROM calls ORDER BY created_at DESC;")
        return cur.fetchall()


@router.post("/webhook")
async def retell_webhook(request: Request):
    payload = await request.json()
    call_id = payload.get("call_id")
    transcript = payload.get("transcript")

    if not call_id or not transcript:
        raise HTTPException(status_code=400, detail="Missing call_id or transcript")

    summary = generate_summary(transcript)

    with DBSession() as cur:
        cur.execute(
            """
            UPDATE calls
            SET outcome = %s, transcript = %s, summary = %s
            WHERE id = %s
            RETURNING *;
            """,
            (
                summary.get("call_outcome"),
                payload,
                summary,
                call_id,
            ),
        )
        result = cur.fetchone()

    return {"message": "Call updated", "call": result}
