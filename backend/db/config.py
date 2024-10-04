from bson import UuidRepresentation
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings 
import logging

class Settings(BaseSettings):
    mongodb_url: str = 'mongodb://localhost:27017'
    database_name: str = 'devJobsDB'
    job_collection: str = 'jobs'
    user_collection: str = 'users'

    class Config:
        env_file = ".env"

settings = Settings()

# Using uvicorn's logger
logger = logging.getLogger("uvicorn")

try:
    client = AsyncIOMotorClient(settings.mongodb_url, uuidRepresentation='standard')
    db = client[settings.database_name]
    logging.info(f"Connected to MongoDB at {settings.mongodb_url}")
except Exception as e:
    logging.error(f"Failed to connect to MongoDB: {e}")