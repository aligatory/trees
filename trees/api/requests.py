from http import HTTPStatus

from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from requests import Response

router = APIRouter()
itsm_base = 'https://training-2.itsm365.com/sd/services/rest/'
access_key = '5aa5a90f-f56f-4be9-8e44-7738f5ce6420'
import requests

success = 'http://185.189.14.105/success'


@router.get('/')
async def create_request(last_name: str, first_name: str, patronymic: str,
                         phone_number: str, wants_to_grow: str,
                         request_type: str):
    response: Response = requests.post(f'{itsm_base}create/serviceCall$growingTree?accessKey={access_key}',
                                       json={'metaClass': 'serviceCall$growingTree',
                                             'agreement': 'agreement$2994803',
                                             'shortDescr': 'Kek',
                                             'lastName': last_name,
                                             'firstName': first_name,
                                             'treeId': 1,
                                             "isCitizenWants": True if wants_to_grow == 'on' else False,
                                             'telephone': phone_number,
                                             'patronymic': patronymic})
    if response.status_code == HTTPStatus.CREATED:
        return RedirectResponse(success)
    else:
        return "error"
