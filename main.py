from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/')
def names():
    return 'again'


class Post(BaseModel):
    id: int
    name: str
    surname: str
    birthday: date

origins = [
    'http://localhost:8080',
    'http://127.0.0.1:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
    allow_credentials = True,
    allow_methods = ['*'],
)
