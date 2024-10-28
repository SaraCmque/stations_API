from fastapi import FastAPI
from app.api.routes.routes import router
from app.api.config.tortoise_config import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
import os

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # Usaremos Aerich para las migraciones
    add_exception_handlers=True,
)

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

app.include_router(router, prefix="/estaciones", tags=["Estaciones"])
