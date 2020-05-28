from http import HTTPStatus
from pathlib import Path

import requests
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import RedirectResponse
from requests import Response
from trees.url import base_url

router = APIRouter()
itsm_base = 'https://training-1.itsm365.com/sd/services/rest'
access_key = 'd766a952-de5b-4b00-a209-a16954eac7e7'

success = f'{base_url}/success'
add_photo_url = f"{itsm_base}/add-file"


@router.post('/')
async def create_request(
    last_name: str = Form(...),
    first_name: str = Form(...),
    phone_number: str = Form(...),
    email: str = Form(...),
    photo: UploadFile = File(...),
):
    response1: Response = requests.post(
        f'{itsm_base}/create-m2m/employee$contactPerson?accessKey={access_key}',
        json={
            'metaClass': 'employee$contactPerson',
            'parent': 'ou$3246521',
            'lastName': last_name,
            'firstName': first_name,
            'email': email,
        },
    )

    response: Response = requests.post(
        f'{itsm_base}/create-m2m/serviceCall$complaint?accessKey={access_key}',
        json={
            'metaClass': 'serviceCall$complaint',
            'client': response1.json()['UUID'],
            'service': 'slmService$3269602',
            'agreement': 'agreement$605301',
            'shortDescr': 'Жалоба на незаконный спил',
            'userName': f'{last_name} {first_name}',
            'phoneNumber': phone_number,
            'userMail': email,
        },
    )
    if response.status_code == HTTPStatus.CREATED:
        res = response.json()
        uuid = res["UUID"]
        print(uuid)
        a = f"{add_photo_url}/{uuid}?accessKey={access_key}&attrCode=photo"
        photo_bytes = await photo.read()
        r = requests.post(
            a, files={'photo': ("photo.png", photo_bytes, "multipart/form-data")}
        )
        print(r.status_code)
        print(r.text)
        return RedirectResponse(success, HTTPStatus.SEE_OTHER.value)
    else:
        print(response.text)
        print(response.status_code)
        return "Произошла ошибка"


path = Path(__file__).parent.parent / "image.png"
