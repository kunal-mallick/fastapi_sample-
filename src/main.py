from fastapi import FastAPI
from src.routers.auth import router

app = FastAPI()
app.include_router(router)