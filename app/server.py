import logging

import urllib3
import uvicorn
from fastapi import FastAPI

from app import settings, api

# don't show the warning message from urllib3
urllib3.disable_warnings()

# start logger
logger = logging.getLogger(__name__)

# start FastApi
app = FastAPI()

# route all api
app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG
    )
