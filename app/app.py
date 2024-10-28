from fastapi import FastAPI
from app.api.config.database import engine
from app.api.models.sqlalchemy_models import Base
from app.api.routes.routes import router
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

Base.metadata.create_all(bind=engine)


app.include_router(router, prefix="/estaciones", tags=["Estaciones"])
