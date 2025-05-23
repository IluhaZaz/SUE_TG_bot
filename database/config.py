from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeMeta

from config.config import config


Base: DeclarativeMeta = declarative_base()

db = config.postgres_db

DATABASE_URL = f"postgresql+asyncpg://{db.db_user}:{db.db_pass}@{db.db_host}:{db.db_port}/{db.db_name}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
