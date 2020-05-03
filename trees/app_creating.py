from fastapi import FastAPI
from trees.api import trees


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(trees.router)
    return app
