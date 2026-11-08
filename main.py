from fastapi import FastAPI, Depends, HTTPException
import models
from router import register, posts, login







app= FastAPI(title="FASTAPI_PROJECT_2")



app.include_router(register.router)
app.include_router(login.router)
app.include_router(posts.router)
