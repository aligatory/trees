from fastapi import FastAPI
from trees.api import index
from trees.api import api


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(index.router)
    app.include_router(api.router, prefix='/requests')
    return app
