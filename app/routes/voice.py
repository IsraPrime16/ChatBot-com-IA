from fastapi import APIRouter
from twilio.twiml.voice_response import VoiceResponse

router = APIRouter()

@router.post("/")
def atender_ligacao():
    response = VoiceResponse()
    response.say(
        "Olá! Você está falando com o assistente virtual. Como posso ajudar?",
        language="pt-BR"
    )
    response.record(
        action="/voice/processar",
        language="pt-BR"
    )
    return str(response)

@router.post("/processar")
def processar_audio():
    response = VoiceResponse()
    response.say(
        "Ainda estou aprendendo, mas em breve responderei por voz!",
        language="pt-BR"
    )
    response.hangup()
    return str(response)