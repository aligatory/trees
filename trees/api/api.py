from http import HTTPStatus
from pathlib import Path
import requests
from fastapi import APIRouter, Form, File, UploadFile
from fastapi.responses import RedirectResponse
from requests import Response
from trees.url import base_url

router = APIRouter()
itsm_base = 'https://training-2.itsm365.com/sd/services/rest'
access_key = 'a1d0e18a-9ffb-4c7c-950c-12c68f50ccb3'

success = f'{base_url}/success'
add_photo_url = f"{itsm_base}/add-file"


@router.post('/')
async def create_request(last_name: str = Form(...), first_name: str = Form(...),
                         phone_number: str = Form(...), email: str = Form(...), photo: UploadFile = File(...)):
    response: Response = requests.post(f'{itsm_base}/create-m2m/serviceCall$complaint?accessKey={access_key}',
                                       json={'metaClass': 'serviceCall$complaint',
                                             'agreement': 'agreement$2994803',
                                             'shortDescr': 'Жалоба на незаконный спил',
                                             'fullnameUser': last_name + first_name,
                                             'phoneNumber': phone_number,
                                             'email': email})
    if response.status_code == HTTPStatus.CREATED:
        res = response.json()
        uuid = res["UUID"]
        print(uuid)
        p = Path(__file__).resolve().parent.parent / "file.png"
        a = f"{add_photo_url}/{uuid}?accessKey={access_key}&attrCode=photo"
        r = requests.post(a, files={'photo': (photo.file.name, open(str(p), "rb"), "multipart/form-data")})
        print(r.status_code)
        print(r.text)
        return RedirectResponse(success, HTTPStatus.SEE_OTHER.value)
    else:
        print(response.text)
        print(response.status_code)
        return "Произошла ошибка"
