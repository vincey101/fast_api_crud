from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import users
from app.core.database import engine
from app.models import user as user_model

# Create database tables
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include routers
app.include_router(users.router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"} 