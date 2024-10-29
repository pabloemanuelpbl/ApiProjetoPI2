from fastapi import FastAPI
from routes import public_router, user_router

app = FastAPI()

app.include_router(public_router)
app.include_router(user_router)