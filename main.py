from fastapi import FastAPI
from routes.index import wizard

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(wizard)

