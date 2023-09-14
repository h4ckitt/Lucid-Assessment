from fastapi import FastAPI
from view.signup import router

app = FastAPI()
app.include_router(router)


@app.get("/ping")
def ping():
    return {"message": "pong"}
