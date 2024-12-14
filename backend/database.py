import os
from databases import Database
from sqlmodel import SQLModel, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_session
from sqlalchemy.orm import sessionmaker

from backend.config import Config


database = Database(Config.DATABASE_URL)

engine = create_async_engine(  # for postgres
    Config.DATABASE_URL,
    echo=True,
    future=True,
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def init_db():
    """Initialize the database by creating tables."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        statement = text("select 'Hello DB'")
        result = await conn.execute(statement)

        print(result.all())
