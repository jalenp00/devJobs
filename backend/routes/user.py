from db.models.user_models import *
from service.auth_service.user_auth_service import *
from fastapi import APIRouter, Depends
from db.config import db, settings
from redis.asyncio import Redis
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
from uuid import uuid4, UUID
from bson.binary import Binary
from db.models.error_models import ErrorModel
from typing import Union
from config.logger import logger
from util.password_converter import *
import json

router = APIRouter()
redis_client = Redis()

user_collection = db[settings.user_collection]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a new user
@router.post('/')
async def signup(user: UserSignUpModel):
    user_doc = user.model_dump()

    user_doc['_id'] = uuid4()
    user_doc['createDate'] = datetime.now()
    user_doc['hashed_password'] = hash_password(user.password)

    result = await user_collection.insert_one(user_doc)

    created_user = await user_collection.find_one({'_id': result.inserted_id})

    response_user = transform_to_response_model(created_user)
    # Generate session ID and store in Redis
    session_id = str(uuid4())

    await redis_client.set(session_id, response_user, ex=3600)  # 1-hour expiry

    return {"access_token": session_id, "token_type": "bearer"}

# Get a user
@router.post('/user')
async def get_user(req: UserRequestModel):
    logger.info(f"Getting user with id: {req.id}")
    id = UUID(req.id)
    user = await user_collection.find_one({'_id': id})
    if not user:
        return {'error': "No user exists"}
    response_user = transform_to_response_model(user)
    return response_user

# Login
@router.post('/login')
async def login(user: UserLoginModel):

    user_doc = user.model_dump()
    authenticated_user = await authenticate_user(user_doc['email'], user_doc['password'])

    if not authenticated_user:
        return {'error': 'Not authenticated'}

    # Create session token
    session_id = str(uuid4())

    # Create redis user object
    user_to_redis = authenticated_user.model_dump_json()

    # Store session in Redis
    await redis_client.set(session_id, user_to_redis, ex=3600)  # 1-hour expiry

    return {"access_token": session_id, "token_type": "bearer"}

