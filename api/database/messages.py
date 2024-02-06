from pymongo import MongoClient
from utils import get_settings
from schema.chat import CreateChat
from models.chat import Message
from bson import ObjectId
from exceptions import QuantGenieException
import datetime
import pymongo

settings = get_settings()

class ChatRepo:

    def __init__(self, connection_string: str = settings.MONGODB_CONNECTION_URL):
        self.client = MongoClient(connection_string)
        self.db = self.client['quant-genie']['chats']
    
    def new_chat(self, chat_create: dict):
        chat_create['last_accessed_date'] = datetime.datetime.now()
        chat_create['chat_history'] = ''
        return str(self.db.insert_one(chat_create).inserted_id)

    def get_chat(self, chat_id: str):
        chat = self.db.find_one({ '_id': ObjectId(chat_id) })
        if not chat:
            raise QuantGenieException('Chat not found')
        return chat
    
    def update_history_time(self, chat_id: str, history:str):
        return self.db.find_one_and_update({ '_id': chat_id }, { '$set': {'chat_history': history, 'last_accessed_date': datetime.datetime.now() } })
    
    def get_chats(self, user_id: str):
        chats = self.db.find({ 'user_id': user_id }).sort('last_accessed_date', pymongo.DESCENDING)
        if not chats:
            raise QuantGenieException('No Chat history found')
        return chats

class MessageRepo:

    def __init__(self, connection_string: str = settings.MONGODB_CONNECTION_URL):
        self.client = MongoClient(connection_string)
        self.db = self.client['quant-genie']['messages']
    
    def get_messages(self, chat_id: str):
        messages =  self.db.find({ 'chat_id': chat_id })
        if not messages:
            raise QuantGenieException('No messages Found')
        return messages

    def add_message(self, chat_id: str, message: dict):
        return self.db.insert_one({ 'chat_id': chat_id, 'input': message.get('input'), 'output': message.get('output'), 'time_of_message': datetime.datetime.now() })