from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from redis.asyncio import Redis

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/user")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    
    username = await Redis.get(token)
    if not username:
        return JSONResponse(content={"error": 'Not authorized'})
    
    return JSONResponse(content={"username": username})