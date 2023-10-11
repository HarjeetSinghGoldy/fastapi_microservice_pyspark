# main.py

from fastapi import FastAPI
from app.api.endpoints import data as data_router

app = FastAPI()

app.include_router(data_router.router, prefix="/data")
