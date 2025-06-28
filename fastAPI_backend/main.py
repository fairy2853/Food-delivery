from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastAPI_backend.core import settings
from fastAPI_backend.routers import app_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(app_router)
