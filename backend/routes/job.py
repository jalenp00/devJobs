from db.models.job_models import *
from fastapi import APIRouter, Query
from config.db import db, settings
from datetime import datetime
from uuid import uuid4, UUID
from bson.binary import Binary
from db.models.error_models import ErrorModel
from typing import Union
from config.logger import logger

router = APIRouter()

job_collection = db[settings.job_collection]

@router.post('/', response_model=Union[JobWrapperModel, ErrorModel])
async def create_job(job: JobRequestModel):
    # Get user input
    job_doc = job.model_dump(by_alias=True)

    # Generate UUID
    job_doc['_id'] = uuid4()

     # Generate create date
    job_doc['datePosted'] = datetime.now()

    job_doc['numApplicants'] = 0

    # Send job_doc to db
    result = await job_collection.insert_one(job_doc)

    # Get user and transform to ResponseModel for frontend
    created_job = await job_collection.find_one({'_id': result.inserted_id})
    response_job = transform_to_response_model(created_job)

    return JobWrapperModel(job=response_job)

@router.get('/', response_model=Union[JobListWrapperModel, ErrorModel])
async def get_all():
    jobs = await job_collection.find().to_list(length=None) 

    if not jobs:
        return ErrorModel(error='Could not retrieve jobs')
    
    job_list = []

    for job in jobs:
        job_list.append(transform_to_response_model(job))
    
    return JobListWrapperModel(jobs=job_list)