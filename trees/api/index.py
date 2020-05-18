from typing import Any
from fastapi import Request
from fastapi import APIRouter
from starlette.templating import Jinja2Templates
from trees.config import service_settings

router = APIRouter()
templetes = Jinja2Templates(directory='trees/templates')


@router.get('/')
async def get_main_page(req: Request):
    return templetes.TemplateResponse("main-page.html", {"request": req, "base_url": service_settings.base_url})


@router.get('/report')
async def get_report_page(req: Request):
    return templetes.TemplateResponse("report.html", {"request": req, "base_url": service_settings.base_url})


@router.get('/volunteers')
async def get_volunteers_page(req: Request):
    return templetes.TemplateResponse("volunteers.html", {"request": req, "base_url": service_settings.base_url})
# @router.get('/success')
# async def ok() -> Any:
#     return 'Заявка успешно оставлена'
#
#
# @router.get('/')
# async def get_page(req: Request) -> Any:
#     return templetes.TemplateResponse('complain.html', {'request': req})