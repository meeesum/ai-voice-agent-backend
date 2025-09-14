from fastapi import APIRouter, Request, HTTPException
import hmac, hashlib
from app.config import settings

router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])

WEBHOOK_SECRET = settings.RETELL_API_KEY  # use your API key for now; if they give a webhook secret, replace it


@router.post("/retell")
async def retell_webhook(req: Request):
    body = await req.body()
    signature = req.headers.get("X-Retell-Signature")

    # optional signature check
    if signature:
        computed_sig = hmac.new(
            key=WEBHOOK_SECRET.encode(),
            msg=body,
            digestmod=hashlib.sha256
        ).hexdigest()
        if not hmac.compare_digest(computed_sig, signature):
            raise HTTPException(status_code=400, detail="Invalid signature")

    event = await req.json()
    # here you can process the event, store summaries, call outcomes, etc.
    print("Received Retell event:", event)
    return {"status": "ok"}
