from fastapi import FastAPI
from routes.chat import chat_router
from routes.user import user_router
from utils import get_settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
import json

from llm.agent import agent_executor
from langchain.load import dumps, loads
from database.messages import ChatRepo

app = FastAPI()
sio = SocketManager(app, cors_allowed_origins=[])

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # can alter with time
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

settings = get_settings()

@app.get('/health')
def health_check():
    return { 'message': 'App is up and running' }

@app.post('/ws')
def socket():
    return {'message': 'Chat Application'}

@sio.on('connect')
async def connect(sid, environ, auth):    
    print('Connected!!', sid)

@sio.on('message')
async def message(sid, message):

    query_dict = loads(json.dumps(message))
    print('New Message', message)
    # response = await agent_executor.acall(query_dict)
    response = { 'output': { 'text': 'Thank you for reaching out to Quant-Genie. Your queries will be resolved in no time.', 'urls': ['http://none.com', 'http://local.com'] }, 'chat_id': 'sajfdhisfh', 'chat_history': "Nah I'd win"}

    await sio.emit('message', dumps(response), to=sid)

@sio.on('disconnect')
async def disconnect(sid):
    print('Disconnected', sid)


app.include_router(chat_router)
app.include_router(user_router)
