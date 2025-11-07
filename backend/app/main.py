from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], # allow requests from frontend in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message" : "Hello World!"}

@app.get("/api/locations")
def location():
    return {"message" : "Hello Locations!"}

@app.get("/api/ghosts")
def ghosts():
    return {"message" : "BOOO..."}
