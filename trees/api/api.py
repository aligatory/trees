from http import HTTPStatus
from pathlib import Path

import aiohttp
import requests
from aiohttp import FormData
from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import RedirectResponse
from requests import Response
from trees.url import base_url

router = APIRouter()
itsm_base = 'https://training-1.itsm365.com/sd/services/rest'
access_key = 'f2f348c8-25c0-4fb4-b819-fc99d421aca7'

success = f'{base_url}/success'
add_photo_url = f"{itsm_base}/add-file"


@router.post('/complaint', status_code=HTTPStatus.CREATED.value)
async def create_request(
        last_name: str = Form(...),
        first_name: str = Form(...),
        phone_number: str = Form(...),
        email: str = Form(...),
        photo: UploadFile = File(...),
):
    uuid = await get_user_uuid(email, first_name, last_name)
    async with aiohttp.ClientSession() as session:
        async with session.post(
                f'{itsm_base}/create-m2m/serviceCall$complaint?accessKey={access_key}',
                json={
                    'metaClass': 'serviceCall$complaint',
                    'client': uuid,
                    'service': 'slmService$3269602',
                    'agreement': 'agreement$605301',
                    'shortDescr': 'Жалоба на незаконный спил',
                    'userName': f'{last_name} {first_name}',
                    'phoneNumber': phone_number,
                    'userMail': email,
                },
        ) as resp:
            res = await resp.json()

    if resp.status == HTTPStatus.CREATED:
        uuid = res["UUID"]
        photo_bytes = await photo.read()
        async with aiohttp.ClientSession() as session:
            data = FormData()
            data.add_field('photo', photo_bytes, filename="photo.png", content_type="multipart/form-data")
            async with session.post(
                    f"{add_photo_url}/{uuid}?accessKey={access_key}&attrCode=photo", data=data
            ) as resp:
                pass

        print(resp.status)
    else:
        print(resp.status)
        return "Произошла ошибка"


async def get_user_uuid(email, first_name, last_name):
    async with aiohttp.ClientSession() as session:
        async with session.post(
                f'{itsm_base}/find/employee$contactPerson?accessKey={access_key}',
                json={'email': email},
        ) as resp:
            json_ = await resp.json()
    if len(json_) == 0:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{itsm_base}/create-m2m/employee$contactPerson?accessKey={access_key}',
                    json={
                        'metaClass': 'employee$contactPerson',
                        'parent': 'ou$3246521',
                        'lastName': last_name,
                        'firstName': first_name,
                        'email': email,
                        'login': email,
                    },
            ) as resp:
                json1 = await resp.json()


        uuid = json1['UUID']
    else:
        uuid = json_[0]['UUID']
    return uuid


@router.post('/grow_on_street', status_code=HTTPStatus.CREATED.value)
async def grow_on_street(
        last_name: str = Form(...),
        first_name: str = Form(...),
        phone_number: str = Form(...),
        email: str = Form(...),
):
    uuid = await get_user_uuid(email, first_name, last_name)
    async with aiohttp.ClientSession() as session:
        async with session.post(
                f'{itsm_base}/create-m2m/serviceCall$growingTree?accessKey={access_key}',
                json={
                    'metaClass': 'serviceCall$growingTree',
                    'client': uuid,
                    'service': 'slmService$3374401',
                    'agreement': 'agreement$605301',
                    'shortDescr': 'Посадка дерева',
                    'userName': f'{last_name} {first_name}',
                    'phoneNumber': phone_number,
                    'lastName': last_name,
                    'firstName': first_name
                },
        ) as resp:
            print(resp.status)
            if resp.status != HTTPStatus.CREATED.value:
                raise HTTPException(HTTPStatus.BAD_REQUEST.value)


@router.post('/grow_on_yard', status_code=HTTPStatus.CREATED.value)
async def grow_on_yard(
        last_name: str = Form(...),
        first_name: str = Form(...),
        phone_number: str = Form(...),
        email: str = Form(...),
):
    uuid = await get_user_uuid(email, first_name, last_name)
    async with aiohttp.ClientSession() as session:
        async with session.post(
                f'{itsm_base}/create-m2m/serviceCall$growingTree?accessKey={access_key}',
                json={
                    'metaClass': 'serviceCall$growingTree',
                    'client': uuid,
                    'service': 'slmService$3349501',
                    'agreement': 'agreement$605301',
                    'shortDescr': 'Посадка дерева',
                    'userName': f'{last_name} {first_name}',
                    'phoneNumber': phone_number,
                    'lastName' : last_name,
                    'firstName':first_name
                },
        ) as resp:
            if resp.status != HTTPStatus.CREATED.value:
                raise HTTPException(HTTPStatus.BAD_REQUEST.value)


path = Path(__file__).parent.parent / "image.png"
