from fastapi import FastAPI
from trees.api import trees
from trees.api import requests


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(trees.router)
    app.include_router(requests.router, prefix='/requests')
    return app
