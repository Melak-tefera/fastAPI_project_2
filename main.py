from fastapi import FastAPI
import models
from router import users, posts


app= FastAPI(title="FASTAPI_PROJECT_2")
app.include_router(users.router)
app.include_router(posts.router)
