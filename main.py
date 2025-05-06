from fastapi import FastAPI
from app.schemas import Message
from app.model import get_reply

app = FastAPI()

@app.post("/chat")
def chat(msg: Message):
    reply = get_reply(msg.message)
    return {"reply": reply}
