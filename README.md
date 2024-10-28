# stations_API - Guia de despliegue
## 1. Configuración del entorno de desarrollo
1. **Clonar el repositorio:**
    git clone https://github.com/SaraCmque/stations_API.git
    cd stations_API

2. **Crear un entorno virtual:**
    python -m venv venv

3. **Activar el entorno virtual:**
    - En Windows: .\venv\Scripts\activate
    - En Linux/macOS: source venv/bin/activate

4. **Instalar las dependencias:**
    pip install -r requirements.txt

5. **Configurar Variables de Entorno:**

    Crea un archivo .env en la raíz del proyecto y añade las variables necesarias. Asegúrate de incluir la variable DATABASE_URL para configurar la conexión a PostgreSQL.

    DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_base_datos

    Reemplaza usuario, contraseña, localhost y nombre_base_datos por los valores específicos de tu configuración de PostgreSQL.

## 2. Ejecución del Proyecto

1. **Iniciar el Servidor de Desarrollo:**
    uvicorn app.app:app --reload

    Esto iniciará el servidor en http://127.0.0.1:8000.

2. **Probar la API:**
    - Accede a la documentación interactiva en Swagger UI: http://127.0.0.1:8000/docs.
    - También puedes ver la documentación en formato ReDoc en: http://127.0.0.1:8000/redoc.