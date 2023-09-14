from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from models.login import SignUp
from view.functions import get_session
from view.signup import router
from models.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


@app.post("/ping")
def ping(user: SignUp, session: Session = Depends(get_session)):
    return {"message": user}
