from fastapi import APIRouter, Request
from twilio.rest import Client
from app.services.ai import gerar_resposta
from app.core.config import *

router = APIRouter()

twilio = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    mensagem = form.get("Body")
    remetente = form.get("From")

    resposta = gerar_resposta(mensagem)

    twilio.messages.create(
        body=resposta,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=remetente
    )

    return "ok"