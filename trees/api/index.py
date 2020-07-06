from typing import Any

from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from trees.url import base_url

router = APIRouter()
templetes = Jinja2Templates(directory='trees/templates')


@router.get('/')
async def get_main_page(req: Request):
    return templetes.TemplateResponse(
        "main-page.html", {"request": req, "base_url": base_url}
    )


@router.get('/report')
async def get_report_page(req: Request):
    return templetes.TemplateResponse(
        "report.html", {"request": req, "base_url": base_url}
    )


@router.get('/volunteers')
async def get_volunteers_page(req: Request):
    return templetes.TemplateResponse(
        "volunteers.html", {"request": req, "base_url": base_url}
    )


@router.get('/city_plant')
async def get_city_plant_page(req: Request):
    return templetes.TemplateResponse('city_plant.html', {'request': req, "base_url": base_url})


@router.get('/yard_plant')
async def get_yard_plant_page(req: Request):
    return templetes.TemplateResponse('yard_plant.html', {'request': req, "base_url": base_url})


@router.get('/success')
async def ok() -> Any:
    return 'Заявка успешно оставлена'


@router.get('/report_form')
async def get_page(req: Request) -> Any:
    return templetes.TemplateResponse('complain.html', {'request': req})


@router.get('/robots.txt')
async def get_robots_txt():
    return open('robots.txt', 'r')
