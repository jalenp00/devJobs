from db.models.user_models import *
from service.auth_service.user_auth_service import *
from fastapi import APIRouter, Depends
from config.db import db, settings
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
redis_client = Redis.from_url('redis://redis:6379')

user_collection = db[settings.user_collection]
job_collection = db[settings.job_collection]

# Create a new user
@router.post('/')
async def signup(user: UserSignUpModel):
    user_doc = user.model_dump()

    user_doc['_id'] = uuid4()
    user_doc['createDate'] = datetime.now()

    user_doc['hashed_password'] = hash_password(user.password)
    del user_doc['password']

    result = await user_collection.insert_one(user_doc)

    created_user = await user_collection.find_one({'_id': result.inserted_id})

    response_user = transform_to_response_model(created_user)

    user_to_redis = response_user.model_dump_json()

    # Generate session ID and store in Redis
    session_id = str(uuid4())

    await redis_client.set(session_id, user_to_redis, ex=3600)  # 1-hour expiry

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

@router.post('/apply')
async def apply_to_job(req: ApplyModel):
    logger.info(f"Applying to job with id: {req.job_id}")
    job_id = UUID(req.job_id)
    user_id = UUID(req.user_id)

    job = await job_collection.find_one({'_id': job_id})
    user = await user_collection.find_one({'_id': user_id})

    if not job:
        return {'error': 'Job does not exist'}
    
    if not user:
        return {'error': 'User does not exist'}
    
    if 'numApplicants' not in job:
        job['numApplicants'] = 0
    
    if 'applicants' not in job:
        job['applicants'] = []
        
    job['numApplicants'] += 1
    job['applicants'].append(user_id)

    if 'appliedJobs' not in user:
        user['appliedJobs'] = []

    user['appliedJobs'].append(job_id)

    await job_collection.update_one({'_id': job_id}, {'$set': job})

    await user_collection.update_one({'_id': user_id}, {'$set': user})

    return {'success': 'Applied to job'}

