from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "MediReport AI"
    database_url:str
    gemini_api_key:str = ""
    gcp_vision_credentials_path: str = ""
    jwt_secret:str = ""
    jwt_algorithm:str = "HS256"


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

# class Config:
#     env_file = '.env'

settings = Settings()
