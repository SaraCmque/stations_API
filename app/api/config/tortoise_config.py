import os
from dotenv import load_dotenv

load_dotenv()  

TORTOISE_ORM = {
    "connections": {
        "default": os.getenv("DATABASE_URL")
    },
    "apps": {
        "models": {
            "models": ["app.api.models.tortoise_models", "aerich.models"],  # Ruta a los modelos y a Aerich
            "default_connection": "default",
        }
    }
}