"""Module py-web-service"""

import os

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_profiler import PyInstrumentProfilerMiddleware

from .utils.settings import Settings
from .models.nlargest import Input, Output
from .core.common import find_top_n_elements_from_list_minheap


WORKSPACE = os.getenv('WORKSPACE', '/opt/dev')
CONFIG_PATH = os.path.join(WORKSPACE, 'config/env')
PROFILE_PATH = os.path.join(WORKSPACE, 'profiles')

setting = Settings(_env_file=CONFIG_PATH)

app = FastAPI(title="Find Top N Elements in a List API",
              description="To find top n elements in a list, where n is a positive integer",
              version="0.1.0",
              docs_url=setting.docs_url,
              redoc_url=setting.redoc_url,
              openapi_url=setting.openapi_url)

if setting.profile_enable:
    app.add_middleware(
        PyInstrumentProfilerMiddleware,
        server_app=app,
        profiler_output_type="html",
        is_print_each_request=False,
        open_in_browser=False,
        html_file_name=os.path.join(PROFILE_PATH, setting.profile_name),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.post("/api/v1/nlargest", response_model=Output)
async def top_n_elements_api(_input: Input):
    """
    Find top n elements in a list API
    """
    return {"result": find_top_n_elements_from_list_minheap(_input.num_list, _input.top_n)}


@app.get("/chk")
async def health_check():
    """
    Health Check API
    """
    return {"status": "OK"}
