from fastapi import APIRouter, status, Header, Depends, HTTPException
from use_cases.exemplo import static_url_funct

def teste(Host: str | None = Header()):
    print(Host)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid access token"
    )


router = APIRouter()

user_router = APIRouter(dependencies=[Depends(teste)])

@router.get("/")
def home() -> str:
    print("rota aqui")
    return "ola mundo: "

user_router.add_api_route("/{static_url}", static_url_funct,
    methods=['GET'], 
    status_code=status.HTTP_200_OK, 
    description="descricao maneira"
)



