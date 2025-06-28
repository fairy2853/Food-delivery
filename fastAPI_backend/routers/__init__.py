from .default import default_router
from fastapi import APIRouter


app_router = APIRouter()

app_router.include_router(default_router, prefix="/default", tags=["Default"])
