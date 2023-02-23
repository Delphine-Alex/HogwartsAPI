from fastapi import FastAPI
import api

app = FastAPI()

app.include_router(api.router)

@app.get("/")
def read_main():
    return {"Hello": "World"}



