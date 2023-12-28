from typing import AsyncIterable
from fastapi import APIRouter, WebSocket, Depends
from dotenv import load_dotenv
from llm.agent import agent_executor
from langchain.load import dumps, loads
from langchain.callbacks import AsyncIteratorCallbackHandler
import asyncio
from database.messages import ChatRepo
from schema.chat import CreateChat, CreateChatSuccess, UpdateChat
from models.chat import Message, ChatModel
from schema import SuccessMessage
from typing import List
from exceptions import QuantGenieException

from utils import get_settings
import json

settings = get_settings()

chat_router = APIRouter(tags=["chats"])

# async def send_message(query_dict: dict, socket: WebSocket) -> AsyncIterable[str]:
#     callback = AsyncIteratorCallbackHandler()
#     task = asyncio.create_task(
#         agent_executor.acall(query_dict)
#     )
#     try:
#         async for token in callback.aiter():
#             socket.send_text(token)
#     except Exception as e:
#         print(f"Caught exception: {e}")
#     finally:
#         callback.done.set()

#     await task

@chat_router.get('/chat/{chat_id}', response_model=ChatModel)
async def get_chat(chat_id:str, chats: ChatRepo = Depends()):
    chat = chats.get_chat(chat_id)
    return chat

@chat_router.post('/new', response_model=CreateChatSuccess)
async def new_chat(chat: CreateChat, chats: ChatRepo = Depends()):
    chat_id = chats.new_chat(chat)
    return { 'message': 'Chat created successfully', 'chat_id': str(chat_id) }

@chat_router.patch('/chat', response_model=ChatModel)
async def add_message(updated_chat: UpdateChat, chats: ChatRepo = Depends()):
    response = chats.add_chat(updated_chat)
    response['_id'] = str(response['_id'])
    return response

@chat_router.websocket_route('/chat')
async def get_response(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        response = agent_executor.invoke(loads(json.dumps(data)), websocket)
        await websocket.send_json(dumps(response)) 

