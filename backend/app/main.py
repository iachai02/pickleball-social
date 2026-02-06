from fastapi import FastAPI
from app.api.v1 import profiles

app = FastAPI()

app.include_router(profiles.router)

@app.get("/health")
def health():
    return {"status": "healthy", "app": "Rally API"}
