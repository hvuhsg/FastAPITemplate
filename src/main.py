from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from dotenv import get_key  # Create .env file in your project

from .api.main import api_route
from .db import DB


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=get_key(".env", "SESSION_SECRET"))
app.include_router(api_route)


@app.on_event("startup")
def startup():
    DB()  # Init db singleton


@app.on_event("shutdown")
def shutdown():
    db = DB.get_instance()
    db.close()
