from fastapi import FastAPI

from backend.api.routes import (
    router
)

app = FastAPI(
    title="Employee ETL API"
)

app.include_router(
    router
)