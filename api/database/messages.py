from pymongo import MongoClient
from utils import get_settings
from schema.chat import CreateChat
from models.chat import ChatModel
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
        chat_id = self.db.insert_one(chat_create.model_dump()).inserted_id 
        return self.db.find_one({ '_id': chat_id })

    def add_chat(self, updated_chat: ChatModel):
        response = self.db.find_one_and_update({ '_id': ObjectId(updated_chat.id) }, { '$set': { 'messages': updated_chat.model_dump().get('messages') } }, upsert=False, return_document=ReturnDocument.AFTER)
        return response

    def get_chat(self, chat_id: str):
        chat = self.db.find_one({ '_id': ObjectId(chat_id) })
        if not chat:
            raise QuantGenieException('Chat not found')
        return chat
    
    def get_chats(self, user_id: str):
        print(user_id)
        chats = self.db.find({ 'user_id': user_id })
        if not chats:
            raise QuantGenieException('No Chat history found')
        chat_list = []
        for chat in chats:
            chat['_id'] = str(chat['_id'])
            chat_list.append(chat)
        return chat_list

    