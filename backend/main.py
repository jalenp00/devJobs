# main.py
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import redis.asyncio as redis
import logging

import routes.job as Job
import routes.user as User
import routes.auth.user_auth as UAUTH
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Initialize Redis
Redis = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global Redis
    Redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
    try:
        yield
    finally:
        await Redis.close()

app.router.lifespan_context = lifespan

app.include_router(Job.router, prefix='/job', tags=['Job'])
app.include_router(User.router, prefix='/user', tags=['User'])
app.include_router(UAUTH.router, prefix='/auth', tags=['UAUTH'])