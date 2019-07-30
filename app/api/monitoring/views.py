from fastapi import APIRouter
from starlette.responses import PlainTextResponse
from starlette.status import HTTP_200_OK

from app import __version__

router = APIRouter()


def _get_service_info():
    return {
        "service": "MT Driver",
        "version": __version__,
    }


@router.get("/ping", status_code=HTTP_200_OK)
async def get_pong_response():
    return PlainTextResponse("PONG")


@router.get("/version", status_code=HTTP_200_OK)
def get_version():
    return _get_service_info()


@router.get("/healthcheck", status_code=HTTP_200_OK)
async def get_health_check():
    info = _get_service_info()
    info.update({"status": "OK"})
    return info
