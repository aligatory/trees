import uvicorn
from starlette.staticfiles import StaticFiles
from trees.app_creating import create_app

app = create_app()
app.mount('/static', StaticFiles(directory='trees/static'), name='static')
