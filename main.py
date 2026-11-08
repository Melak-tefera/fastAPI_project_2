from fastapi import FastAPI
import models
from router import register, posts


app= FastAPI(title="FASTAPI_PROJECT_2")
app.include_router(register.router)
app.include_router(posts.router)
