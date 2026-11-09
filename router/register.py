from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import Usercreate, Userread
from security import hased_password

router =APIRouter(tags=["Register"])

@router.post("/register", response_model=Userread)
def register(name: Usercreate, db: Session=Depends(get_db)):
    user_taken= db.query(User).filter(User.username==name.username).first()
    if user_taken:
        raise HTTPException(status_code=400, detail="username already taken")
    user= User(name=name.name, username= name.username, hashed_password= hased_password(name.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


