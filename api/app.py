from fastapi import FastAPI
from routes.chat import chat_router
from routes.user import user_router
from utils import get_settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
from langchain.load import dumps, loads
import json

from llm.agent import agent_executor
from utils import summarizer_chain
from schema.chat import UserMessage
from jobs.chat import add_to_chat
from rq import Queue, Worker
import redis

app = FastAPI()
sio = SocketManager(app, cors_allowed_origins=[])
settings = get_settings()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # can alter with time
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
redis_conn = redis.from_url('redis://redis-server:6379')
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
    message = loads(json.dumps(message))
    try:
        # agent_response = await agent_executor.acall(message.get('llmInput')) 
        print(message)
        agent_response = {
            'output': "Nah, I'd win",
            'chat_history': "Let's go you bozos"
        }  
        summ_message = f"""User: {message.get('llmInput').get('input')} \n QuantGenie: {agent_response.get('output')}"""
        summarizer = summarizer_chain.invoke({ 
                'history': message.get('llmInput').get('chat_history'), 
                'message': summ_message 
                })
        response = { 
            'output': {
                'text': agent_response.get('output')
                }, 
                'chat_history': summarizer, 
                'chatId': message.get('chatId'), 
                'userId': message.get('userId')
            }
        await sio.emit('message', dumps(response), to=sid)
    except Exception as e:
        response = { 
            'output': { 
                'text': str(e), 
                'error': True, 
                'images': [] 
                }, 
                'chat_history': message.get('chat_history'), 
                'chatId': message.get('chatId'), 
                'userId': message.get('userId')
            }
        await sio.emit('message', dumps(response), to=sid)
    
    task_queue.enqueue(add_to_chat,
            user_id=message.get('userId'), 
            message={ 
                'input': message.get('llmInput').get('input'), 
                'output': response.get('output') 
                } , 
            chat_id=message.get('chatId'), 
            chat_history=response.get('chat_history'))
    return

@sio.on('disconnect')
async def disconnect(sid):
    print('Disconnected', sid)


app.include_router(chat_router)
app.include_router(user_router)