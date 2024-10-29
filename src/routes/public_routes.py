from fastapi import APIRouter

public_router = APIRouter()

@public_router.get("/")
def home() -> str:
    print("rota aqui")
    return "ola mundo: "