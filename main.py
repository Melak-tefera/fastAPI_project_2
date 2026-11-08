from fastapi import FastAPI, Depends, HTTPException
from models import User
from router import register, posts, login
from database import get_db
from sqlalchemy.orm import Session
import jwt
from fastapi.security import OAuth2AuthorizationCodeBearer
from security import SECRET_KEY, ALGORITHM


app= FastAPI(title="FASTAPI_PROJECT_2")
oauth2_scheme= OAuth2AuthorizationCodeBearer(tokenUrl="login")

def get_current_user(token:str=Depends(oauth2_scheme), db: Session= Depends(get_db)):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(data["sub"])
    except Exception:
        raise HTTPException(401, "Bad or expired token")
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(401, "User no longer exists")
    return user
app.include_router(register.router)
app.include_router(login.router)
app.include_router(posts.router)
