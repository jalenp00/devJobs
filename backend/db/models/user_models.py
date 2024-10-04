from pydantic import BaseModel, Field
from typing import List, Optional
from uuid  import UUID, uuid4
from datetime import datetime
import bcrypt

class UserModel(BaseModel):
    id: UUID = Field(uuid4(), alias="_id")
    name: str
    email: str
    hashed_password: str
    createDate: datetime

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class UserSignUpModel(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class UserLoginModel(BaseModel):
    email: str
    password: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class UserResponseModel(BaseModel):
    id: str 
    name: str
    email: str
    createDate: datetime

class UserRequestModel(BaseModel):
    id: str

def transform_to_response_model(user: dict) -> UserResponseModel:
    return UserResponseModel(
        id=str(user.get('_id')),
        name=user.get('name'),
        email=user.get('email'),
        createDate=user.get('createDate'),
    )
