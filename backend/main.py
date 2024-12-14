from fastapi import FastAPI
from backend.apples.routes import apple_router
from backend.database import init_db
from contextlib import asynccontextmanager


# the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("server is stopping")


# app = FastAPI()
version = "v1"

app = FastAPI(
    title="Apples",
    description="A REST API for an apples web service",
    lifespan=lifespan,
)

app.include_router(apple_router, tags=["apples"])
