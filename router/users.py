from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import Usercreate, Userread

router =APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=Userread)
def create_user(name: Usercreate, db: Session=Depends(get_db)):
    user= User(name=name.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("", response_model=list[Userread])
def get_all_users(db:Session=Depends(get_db)):
    user= db.query(User).all()
    return user

@router.get("/{id}", response_model= Userread)
def get_user_byid(id:int, db:Session=Depends(get_db)):
    user= db.query(User).filter(User.id==id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user is not found")
    return user
