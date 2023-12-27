from typing import AsyncIterable
from fastapi import APIRouter, WebSocket
from dotenv import load_dotenv
from llm.agent import agent_executor
from langchain.load import dumps, loads
from langchain.callbacks import AsyncIteratorCallbackHandler
import asyncio

import json

load_dotenv()

chat_router = APIRouter()

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


@chat_router.websocket_route('/chat')
async def get_response(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        response = agent_executor.invoke(loads(json.dumps(data)), websocket)
        await websocket.send_json(dumps(response))

