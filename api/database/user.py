from pymongo import MongoClient, ReturnDocument
from utils import get_settings
from schema.user import UserCreate, UserPatch
from exceptions import QuantGenieException
from bson import ObjectId

settings = get_settings()

class UserRepo:

    def __init__(self, connection_string: str = settings.MONGODB_CONNECTION_URL):
        self.client = MongoClient(connection_string)
        self.db = self.client['quant-genie']['user']
    
    def create_user(self, new_user: UserCreate):
        user = self.db.find_one({ 'email': new_user.email })
        if user:
            raise QuantGenieException('User already exist')
        return self.db.insert_one(new_user.model_dump()).inserted_id
    
    def get_user(self, user_id: str):
        user = self.db.find_one({ '_id': ObjectId(user_id) })
        if not user:
            raise QuantGenieException('User not found')
        return user

    def get_user_by_email(self, email: str):
        user = self.db.find_one({ 'email': email })
        if not user:
            raise QuantGenieException('User not found')
        return user
    
    def patch_user(self, partial_user: UserPatch, user_id: str):
        return self.db.find_one_and_update({ '_id': ObjectId(user_id) }, { '$set': partial_user.model_dump(exclude_none=True)}, upsert=False, return_document=ReturnDocument.AFTER)



    