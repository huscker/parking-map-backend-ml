from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import ORJSONResponse

from controllers import ready
from services.db import connect_db, init_db

import exceptions
import sentry_sdk

sentry_sdk.init(
    dsn="https://4b23365d3a9b4264903ba3f26e4992b0@o4504146862014464.ingest.sentry.io/4504146889211904",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI()
app.include_router(ready.router)


@app.on_event("startup")
async def startup():
    await connect_db()
    await init_db()


@app.exception_handler(Exception)
async def unicorn_base_exception_handler(request: Request, exc: Exception):
    error = exceptions.ServerError(debug=str(exc))

    return ORJSONResponse(
        status_code=error.status_code,
        content=error.to_json(),
    )


@app.exception_handler(exceptions.ApiException)
async def unicorn_api_exception_handler(request: Request, exc: exceptions.ApiException):
    return ORJSONResponse(status_code=exc.status_code, content=exc.to_json())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
