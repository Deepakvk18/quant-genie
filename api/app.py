from fastapi import FastAPI
from routes.chat import chat_router
from routes.user import user_router
from utils import get_settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
import os
import json

from llm.agent import agent_executor
from langchain.load import dumps, loads
from database.messages import ChatRepo
from exceptions import QuantGenieException
import uvicorn

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

@app.sio.on('join')
async def handle_join(sid, *args, **kwargs):
    print(f'User joined in {sid}')
    await sio.emit('join', {'sid': sid})

@app.sio.on('client_connect_event')
async def handle_client_connect_event(sid, *args, **kwargs): # (!)
    await app.sio.emit('server_antwort01', {'data': 'connection was successful'})    

@app.sio.on('client_start_event')
async def handle_client_start_event(sid, *args, **kwargs): # (!)
    print('Server says: start_event worked')
    await app.sio.emit('server_antwort01',{'data':'start event worked'})

@sio.on('connect')
async def connect(sid, environ, auth):
    # await sio.emit('connect', {'sid': sid})
    print('Connected!!', sid)

@sio.on('message')
async def message(sid, message):

    query_dict = loads(json.dumps(message))
    response = await agent_executor.acall(query_dict)

    await sio.emit('message', dumps(response), to=sid)

@sio.on('disconnect')
async def disconnect(sid):
    print('Disconnected', sid)


app.include_router(chat_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)