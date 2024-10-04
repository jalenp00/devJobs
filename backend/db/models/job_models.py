from pydantic import BaseModel, Field
from typing import List, Optional
from uuid  import UUID, uuid4
from datetime import datetime

class JobModel(BaseModel):
    id: UUID = Field(uuid4(), alias="_id")
    userId: UUID
    company: str
    title: str
    location: str
    minSalary: int
    maxSalary: int
    description: str
    techStack: List[str]
    yearsNeeded: int
    datePosted: datetime
    contract: bool
    type: str
    daysInOffice: Optional[int] = None
    numApplicants: int

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class JobRequestModel(BaseModel):
    company: str
    title: str
    location: str
    minSalary: int
    maxSalary: int
    description: str
    techStack: List[str]
    yearsNeeded: int
    contract: bool
    type: str
    daysInOffice: Optional[int] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class JobResponseModel(BaseModel):
    id: str
    company: str
    title: str
    location: str
    minSalary: int
    maxSalary: int
    description: str
    techStack: List[str]
    yearsNeeded: int
    datePosted: datetime
    contract: bool
    type: str
    daysInOffice: Optional[int] = None
    numApplicants: int

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

# Wrapper Models
class JobWrapperModel(BaseModel):
    job: JobResponseModel

class JobListWrapperModel(BaseModel):
    jobs: List[JobResponseModel]

# Transform functions
def transform_to_response_model(job: dict) -> JobResponseModel:
    return JobResponseModel(
        id = str(job.get('_id')),
        company = job.get('company'),
        title = job.get('title'),
        location = job.get('location'),
        minSalary = job.get('minSalary'),
        maxSalary = job.get('maxSalary'),
        description = job.get('description'),
        techStack = job.get('techStack'),
        yearsNeeded = job.get('yearsNeeded'),
        datePosted = job.get('datePosted'),
        contract = job.get('contract'),
        type = job.get('type'),
        daysInOffice = job.get('daysInOffice'),
        numApplicants = job.get('numApplicants')
    )