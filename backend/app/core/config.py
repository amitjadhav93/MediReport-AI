from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MediReport AI"
    database_url:str
    gemini_api_key:str = ""
    gcp_vision_credentials_path: str = ""
    jwt_secret:str = ""
    jwt_algorithm:str = "HS256"

class Config:
    env_file = '.env'

settings = Settings()
