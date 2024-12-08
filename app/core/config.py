from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "User CRUD API"
    DATABASE_URL: str = "sqlite:///./sql_app.db"
    
    class Config:
        case_sensitive = True

settings = Settings() 