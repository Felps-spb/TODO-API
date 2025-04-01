from fastapi import FastAPI

from .database.core import engine, Base
from .models.todo import Todo
from .models.user import User
from .api import register_routes

app = FastAPI()

register_routes(app)