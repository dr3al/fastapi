from contextlib import asynccontextmanager

from fastapi import FastAPI
from api.router import common_router

from core.handlers import register_exception_handlers
from core.database import Base, engine

# декоратор из модуля contextlib в Python, который создаёт асинхронный контекстный менеджер
# позволяет определять фабричную функцию для менеджеров асинхронного контекста оператора async with
# без необходимости создавать класс или реализовывать методы __aenter__() и __aexit__() по отдельности.
@asynccontextmanager
# выполняет действия при запуске и остановке
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # закрывает все соединения и освобождает ресурсы
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(common_router)
register_exception_handlers(app)
