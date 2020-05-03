from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_page() -> Any:
    return 'kek'
