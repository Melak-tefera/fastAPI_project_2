from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import Usercreate, Userread
from security import verify_password, create_token
from fastapi.security import OAuth2PasswordRequestForm

router =APIRouter(tags=["Login"])

@router.post("/login", response_model=Userread)
def login(form: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    
    user = db.query(User).filter(User.username == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(401, "Wrong name or password")
    return {"access_token": create_token(user.id), "token_type": "bearer"}


