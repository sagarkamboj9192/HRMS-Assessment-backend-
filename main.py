import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrm_backend.config.v1.settings")
django.setup()

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from starlette.middleware.cors import CORSMiddleware

from hrm_backend.config.v1.api_config import api_config
from hrm_backend.core.fastapi_app import connect_router as connect_router_v1

from hrm_backend.models.v1.schemas.exception_handler import ExceptionHandlerResponse


app = FastAPI(title=api_config.PROJECT_NAME,docs_url="/api/docs",redoc_url=None,openapi_url="/api/openapi.json")

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exception: RateLimitExceeded):
    api_response = ExceptionHandlerResponse(
        status=False,
        message="Rate limit exceeded. Try again later.",
        data={},
        status_code=429,
    )

    return JSONResponse(
        content=api_response.model_dump(), status_code=api_response.status_code
    )


if api_config.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in api_config.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(connect_router_v1, prefix=api_config.API_VER_STR_V1)
