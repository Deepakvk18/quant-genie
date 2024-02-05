from functools import lru_cache
import config
from passlib.context import CryptContext
from dotenv import load_dotenv
from google.cloud import storage
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

# storage_client = storage.Client(project=os.getenv('GCP_PROJECT_ID'))
# bucket = storage_client.bucket(os.getenv('GCP_STORAGE_BUCKET'))

@lru_cache
def get_settings():
    load_dotenv()
    return config.Settings()

settings = get_settings()


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


SUMMARIZER_PROMPT = """
You are a helpful summarizer. Everytime I give you a history and current message, you summarize them for me in less than 2000 words. Summarize that user asked this and Genie told that. 

HISTORY: {history}

CURRENT MESSAGE: {message}
"""
summarizer = GoogleGenerativeAI(model='gemini-pro', google_api_key=settings.GOOGLE_API_KEY)
prompt = PromptTemplate.from_template(template=SUMMARIZER_PROMPT)
summarizer_chain = prompt | summarizer
    

    