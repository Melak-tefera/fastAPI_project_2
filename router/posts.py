from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, Post
from schemas import Postcreate, Postread
from auth import get_current_user

router = APIRouter(tags=["Posts"])

@router.post("/posts", response_model=Postread)
def create_post(title:Postcreate,db:Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    post= Post(title=title.title, user_id=current_user.id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
@router.get("/posts", response_model=list[Postread])
def get_user_posts(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    posts=db.query(Post).filter(Post.user_id==current_user.id).all()
    return posts




