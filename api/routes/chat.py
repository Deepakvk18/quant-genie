from fastapi import APIRouter, Depends, Security
from database.messages import ChatRepo
from schema.chat import CreateChat, CreateChatSuccess, UpdateChat, Chats
from models.chat import ChatModel
from utils import get_settings
from fastapi_jwt import JwtAuthorizationCredentials
from utils import get_settings

from .extensions import access_security

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

@chat_router.get('/chats', response_model=Chats)
async def get_chats(credentials: JwtAuthorizationCredentials = Security(access_security), chat: ChatRepo = Depends()):
    user_id = credentials.subject.get('userId')
    chats = chat.get_chats(user_id)
    return { 'chats': chats }



async def add_message(updated_chat: UpdateChat, chats: ChatRepo = Depends()):
    response = chats.add_chat(updated_chat)
    response['_id'] = str(response['_id'])
    return response

# @chat_router.websocket_route('/chat')
# async def get_response(websocket: WebSocket):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_json()
#             input_dict = loads(json.dumps(data))
#             await manager.send_message(input_dict)
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)



