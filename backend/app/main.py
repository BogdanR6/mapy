from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import APP_ENV, FRONTEND_URL
from app.db.connection import init_db
from app.api.routes_location import router as location_router

app = FastAPI()

# Database setup
init_db()

# Middleware
if APP_ENV == "development":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[FRONTEND_URL],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Routers
app.include_router(location_router)

@app.get("/")
def root():
    return {"message": "Server Running"}
