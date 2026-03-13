from fastapi import APIRouter

router = APIRouter()

@router.post("/webhook/payment")

async def payment_webhook(payload: dict):

    print("Payment confirmed", payload)

    return {"status": "received"}