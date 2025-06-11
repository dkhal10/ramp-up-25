from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()


r = redis.Redis(host='localhost', port=6379, db=0)

class Message(BaseModel):
    message: str

@app.post("/publish")
def publish_message(msg: Message):
    r.publish("input", msg.message)
    return {"status": "Message published", "message": msg.message}
