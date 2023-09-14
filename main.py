from fastapi import FastAPI
from view.signup import router
from view.post import post_router
from models.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
app.include_router(post_router)


@app.post("/ping")
def ping():
    return {"message": "pong"}
