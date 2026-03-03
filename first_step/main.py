from fastapi import FastAPI, status, Response
from fastapi.responses import JSONResponse

app = FastAPI(title="Test APP", version="0.1")

users = {
    1:{"name": "Petr","email": "a@example.com", "age" : 34},
    2:{"name": "Elena","email": "b@example.com", "age" : 22},
    3:{"name": "Vladimir","email": "c@example.com", "age" : 45},
    4:{"name": "Анатолий","email": "d@example.com", "age" : 95},
    5:{"name": "Victor","email": "e@example.com", "age" : 15},
    6:{"name": "Eva","email": "f@example.com", "age" : 10},
}

clinics = MOCK_CLINICS = [
    {
        "id": 1,
        "name": "Городская поликлиника №1",
        "city": "Москва",
        "district": "Центральный",
        "address": "ул. Тверская, 15",
        "free_slots": 5,
        "rating": 4.5,
        "phone": "+7 (495) 123-45-67",
        "specializations": ["терапия", "хирургия", "кардиология"]
    },
    {
        "id": 2,
        "name": "Медицинский центр Здоровье+",
        "city": "Москва",
        "district": "Центральный",
        "address": "ул. Арбат, 25",
        "free_slots": 2,
        "rating": 4.8,
        "phone": "+7 (495) 234-56-78",
        "specializations": ["стоматология", "косметология", "дерматология"]
    },
    {
        "id": 3,
        "name": "Клиника Семейный доктор",
        "city": "Москва",
        "district": "Северный",
        "address": "ул. Дмитровское шоссе, 50",
        "free_slots": 8,
        "rating": 4.2,
        "phone": "+7 (495) 345-67-89",
        "specializations": ["педиатрия", "гинекология", "урология"]
    },
    {
        "id": 4,
        "name": "Диагностический центр Инвитро",
        "city": "Москва",
        "district": "Южный",
        "address": "ул. Варшавское шоссе, 125",
        "free_slots": 0,
        "rating": 4.6,
        "phone": "+7 (495) 456-78-90",
        "specializations": ["лабораторная диагностика", "УЗИ", "МРТ"]
    },
    {
        "id": 5,
        "name": "Стоматологическая клиника Дентал",
        "city": "Москва",
        "district": "Западный",
        "address": "пр-т Вернадского, 80",
        "free_slots": 3,
        "rating": 4.7,
        "phone": "+7 (495) 567-89-01",
        "specializations": ["стоматология", "ортодонтия", "имплантология"]
    },
    {
        "id": 6,
        "name": "Поликлиника №3",
        "city": "Санкт-Петербург",
        "district": "Центральный",
        "address": "Невский пр-т, 100",
        "free_slots": 4,
        "rating": 4.0,
        "phone": "+7 (812) 123-45-67",
        "specializations": ["терапия", "неврология", "офтальмология"]
    },
    {
        "id": 7,
        "name": "Европейский медицинский центр",
        "city": "Санкт-Петербург",
        "district": "Петроградский",
        "address": "ул. Ленина, 20",
        "free_slots": 1,
        "rating": 4.9,
        "phone": "+7 (812) 234-56-78",
        "specializations": ["хирургия", "онкология", "гастроэнтерология"]
    },
    {
        "id": 8,
        "name": "Клиника Скандинавия",
        "city": "Санкт-Петербург",
        "district": "Василеостровский",
        "address": "Средний пр-т, 40",
        "free_slots": 6,
        "rating": 4.4,
        "phone": "+7 (812) 345-67-89",
        "specializations": ["кардиология", "эндокринология", "пульмонология"]
    }
]


@app.get("/user/{id}")
def index(r: Response, id: int):
    user_data = users.get(id)
    if user_data:
        r.status_code = status.HTTP_200_OK
        return user_data
    else:
        r.status_code = status.HTTP_404_NOT_FOUND
        return {
            "error": True,
            "message": "User not found!"
        }


@app.put("/user/{id}")
def index(id: int, name:str, email:str, age:int):
    user_data = users.get(id)
    if not user_data:
        return JSONResponse({"error": True, "message": "User not found!"}, 404)
    else:
        users[id] = {
            "name": name,
            "email": email,
            "age": age
        }
        return JSONResponse(users.get(id), 200)



@app.get("/clinics/{city}")
def get_clinics(city: str, district: str, limit: int, rating: int = 0):
    result = []
    for clinic in clinics:
        if city != clinic.get("city"):
            continue
        elif district != clinic.get("district"):
            continue
        elif rating > clinic.get("rating"):
            continue

        result.append(clinic)

    return result[:limit]
