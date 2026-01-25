# 🤖 AI Bot – WhatsApp + Ligações (Python)

Este repositório contém um **chatbot de IA** em Python usando **FastAPI**, integrado ao **WhatsApp e chamadas telefônicas via Twilio**, preparado para evoluir de projeto pessoal para produto comercial.

---

## 📦 Stack
- Python 3.11+
- FastAPI
- Twilio (WhatsApp + Voice)
- OpenAI (texto)
- Whisper (STT – futuro)
- TTS (voz – futuro)

---

## 📁 Estrutura do projeto
```
ai-bot/
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── routes/
│   │   ├── whatsapp.py
│   │   └── voice.py
│   └── services/
│       └── ai.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Instalação
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Variáveis de ambiente
Crie um arquivo `.env` baseado no `.env.example`

```
OPENAI_API_KEY=sk-xxxx
TWILIO_ACCOUNT_SID=xxxx
TWILIO_AUTH_TOKEN=xxxx
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

---

## ▶️ Executar
```bash
uvicorn app.main:app --reload
```

---

## 🧠 app/main.py
```python
from fastapi import FastAPI
from app.routes import whatsapp, voice

app = FastAPI(title="AI Bot WhatsApp + Voice")

app.include_router(whatsapp.router, prefix="/webhook")
app.include_router(voice.router, prefix="/voice")

@app.get("/")
def health():
    return {"status": "online"}
```

---

## 🔧 app/core/config.py
```python
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
```

---

## 🧠 app/services/ai.py
```python
from openai import OpenAI

client = OpenAI()

def gerar_resposta(mensagem: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um atendente virtual educado, claro e profissional."
                )
            },
            {"role": "user", "content": mensagem}
        ]
    )
    return response.choices[0].message.content
```

---

## 💬 app/routes/whatsapp.py
```python
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
```

---

## ☎️ app/routes/voice.py
```python
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
```

---

## 📄 requirements.txt
```
fastapi
uvicorn
python-dotenv
twilio
openai
```

---

## 🚀 Próximos passos
- Implementar STT (Whisper)
- Implementar TTS
- Memória de conversa (Redis / DB)
- Transferência para humano
- Docker + Deploy

---

🔥 Projeto pronto para crescer de **pessoal → comercial**.

