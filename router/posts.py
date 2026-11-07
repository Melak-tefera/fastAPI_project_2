from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, Post
from schemas import Postcreate, Postread

router = APIRouter(tags=["Posts"])

@router.post("users/{id}/posts", response_model=Postread)
def create_post_per_user(id:int, title:Postcreate,db:Session=Depends(get_db)):
    user= db.query(User).filter(User.id==id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user is not found")
    post= Post(title=title.title)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
@router.get("/users/{user_id}/posts", response_model=list[Postread])
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts


@router.get("/posts", response_model=list[Postread])
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

