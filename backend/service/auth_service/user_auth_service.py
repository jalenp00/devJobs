from config.db import db, settings
from db.models.user_models import *
from config.logger import logger
import bcrypt

user_collection = db[settings.user_collection]

async def authenticate_user(email: str, password: str):
    user = await user_collection.find_one({'email': email})

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user['hashed_password'].encode('utf-8')):
        return False

    returned_user = transform_to_response_model(user)
    
    return returned_user