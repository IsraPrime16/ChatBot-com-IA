from fastapi import FastAPI
from app.routes import whatsapp, voice

app = FastAPI(title="AI Bot WhatsApp + Voice")

app.include_router(whatsapp.router, prefix="/webhook")
app.include_router(voice.router, prefix="/voice")

@app.get("/")
def health():
    return {"status": "online"}