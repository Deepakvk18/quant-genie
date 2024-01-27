from functools import lru_cache
import config
import os
from passlib.context import CryptContext
from dotenv import load_dotenv
from google.cloud import storage
import io
import matplotlib.pyplot as plt
import logging

# storage_client = storage.Client(project=os.getenv('GCP_PROJECT_ID'))
# bucket = storage_client.bucket(os.getenv('GCP_STORAGE_BUCKET'))
logging.getLogger('passlib').setLevel(logging.ERROR)

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

# def upload_to_cloud(matplotlib_fig):
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
    
#     blob = bucket.blob('DESTINATION_BLOB_NAME.png')

#     blob.upload_from_string(
#     buf.getvalue(),
#     content_type='image/png')
#     buf.close()

#     return blob.public_url