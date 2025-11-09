import os

APP_ENV = os.getenv("APP_ENV", "development")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8080")
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/app.db")

