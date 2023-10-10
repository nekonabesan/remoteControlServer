from fastapi import FastAPI
from api.routers import controller

app = FastAPI()
app.include_router(controller.router)