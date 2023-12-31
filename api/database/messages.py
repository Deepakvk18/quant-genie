from pymongo import MongoClient
from utils import get_settings
from models.chat import Message
from schema.chat import CreateChat, UpdateChat
from typing import List
from pymongo import ReturnDocument
from bson import ObjectId
from exceptions import QuantGenieException

settings = get_settings()

class ChatRepo:

    def __init__(self, connection_string: str = settings.MONGODB_CONNECTION_URL):
        self.client = MongoClient(connection_string)
        self.db = self.client['quant-genie']['chats']
    
    def new_chat(self, chat_create: CreateChat):
        return self.db.insert_one(chat_create.model_dump(), ).inserted_id

    def add_chat(self, updated_chat: UpdateChat):
        response = self.db.find_one_and_update({ '_id': ObjectId(updated_chat.chat_id) }, { '$set': { 'messages': updated_chat.model_dump().get('messages') } }, upsert=False, return_document=ReturnDocument.AFTER)
        return response

    def get_chat(self, chat_id: str):
        chat = self.db.find_one({ '_id': ObjectId(chat_id) })
        if not chat:
            raise QuantGenieException('Chat not found')
        return chat



    