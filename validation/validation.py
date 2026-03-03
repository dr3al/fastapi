from fastapi import FastAPI
from fastapi.responses import JSONResponse

from pydantic import BaseModel, EmailStr, field_validator, Field, status, Response

from typing import List, Optional


class BaseUser(BaseModel):
    username: str = Field(min_length = 4, max_length=19)
    name: str
    email: str
    #email: EmailStr - Встроенная в pydantic валидация Email. Тогда не нужно писать свой метод
    about: Optional[str] = None
    age: int = Field(ge=18, le=99)

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        return value


class CreateUser(BaseUser):
    id: int
    password: str


class UpdateUser(BaseModel):
    about: str


users = []

app = FastAPI()
@app.get("/")
def root():
    # Возвращаем статус код через JSONResponse объект
    return JSONResponse({"Hello": "World"}, status_code = status.HTTP_200_OK)


@app.post("/users", status_code=201)
def create_user(response: Response, user: CreateUser):
    # Получили объект пользователя в представлении "CreateUser" и добавили в список users.
    users.append(user)
    # Возвращаем статус код через объект response
    response.status_code = status.HTTP_201_CREATED
    return {"message": "User created"}


@app.get("/users")
def get_user() -> List[BaseUser]:
    # Собираем всех пользователей в представлении "BaseUser"
    return [BaseUser(**user.dict()) for user in users]
