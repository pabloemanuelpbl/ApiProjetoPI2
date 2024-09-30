from fastapi import FastAPI
from routes import router, user_router

app = FastAPI()

app.include_router(router)
app.include_router(user_router)