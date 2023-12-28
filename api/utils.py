from functools import lru_cache
import config
import os
from passlib.context import CryptContext
from dotenv import load_dotenv

@lru_cache
def get_settings():
    load_dotenv()
    return config.Settings()


class PasswordHasher:

    def __init__(self):
        self.context = CryptContext(schemes=['bcrypt'])
    
    def get_password_hash(self, password):
        return self.context.hash(password)
    
    def verify_password(self, plain_password, hashed_password):
        return self.context.verify(plain_password, hashed_password)