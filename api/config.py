from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    LANGCHAIN_TRACING_V2: str
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str
    LANGCHAIN_ENDPOINT: str
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str
    FMP_API_KEY: str
    MONGODB_CONNECTION_URL: str

    SECRET_KEY: str
    ACCESS_EXPIRY: int
    REFRESH_EXPIRY: int
    GCP_BUCKET_ID: str
    GCP_PROJECT_ID: str
    
    model_config = SettingsConfigDict(env_file=".env")