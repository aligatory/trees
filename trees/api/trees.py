from typing import Any
from fastapi import Request
from fastapi import APIRouter
from starlette.templating import Jinja2Templates

router = APIRouter()
templetes = Jinja2Templates(directory='trees/templates')


@router.get('/success')
async def ok() -> Any:
    return 'Заявка успешно оставлена'


@router.get('/')
async def get_page(req: Request) -> Any:
    return templetes.TemplateResponse('grow_trees.html', {'request': req})
