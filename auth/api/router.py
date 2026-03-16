from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api import books_router
from api import auth_router

common_router = APIRouter()




@common_router.get("/")
def root():
    # Возвращаем статус код через JSONResponse объект
    return JSONResponse({"Hello": "World"}, status_code = status.HTTP_200_OK)


common_router.include_router(books_router)
common_router.include_router(auth_router)