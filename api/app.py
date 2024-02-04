from fastapi import FastAPI
from routes.chat import chat_router
from routes.user import user_router
from utils import get_settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
import json

from llm.agent import agent_executor
from schema.chat import UserMessage
from jobs.chat import add_to_chat
from rq import Queue, Worker
import redis
from fastapi import BackgroundTasks

app = FastAPI()
sio = SocketManager(app, cors_allowed_origins=[])
background_tasks = BackgroundTasks()
settings = get_settings()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # can alter with time
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
redis_conn = redis.from_url(settings.REDIS_URL)
task_queue = Queue("chat_queue", connection=redis_conn)
worker = Worker([task_queue], connection=redis_conn)

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
async def message(sid: str, message: UserMessage):

    print('New Message', message)
    user_id = message.get('userId')
    try:
        # response = await agent_executor.acall(message.get('llmInput))
        # raise QuantGenieException('No error')
        response = { 'output': { 'text': 'Thank you for reaching out to Quant-Genie. Your queries will be resolved in no time.', 'images': ['http://none.com', 'http://local.com'] }, 'chatId': message.get('chatId'), 'chat_history': "Nah I'd win", 'userId': user_id}

        await sio.emit('message', dumps(response), to=sid)
    except Exception as e:
        response = { 'output': { 'text': e.message, 'error': True, 'images': [] }, 'chat_id': 'sajfdhisfh', 'chat_history': "Nah I'd win", 'chatId': message.get('chatId'), 'userId': user_id}
        await sio.emit('message', dumps(response), to=sid)
    
    background_tasks.add_task(add_to_chat, user_id=user_id, message={ 'input': message.get('llmInput').get('input'), 'output': response.get('output') } , chat_id=message.get('chatId'), chat_history=response.get('chat_history'))
    return


    
    

@sio.on('disconnect')
async def disconnect(sid):
    print('Disconnected', sid)


app.include_router(chat_router)
app.include_router(user_router)