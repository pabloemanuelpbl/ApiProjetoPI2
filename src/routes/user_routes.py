from fastapi import APIRouter, status
from use_cases.exemplo import static_url_funct

user_router = APIRouter();

user_router.add_api_route("/{static_url}", static_url_funct,
    methods=['GET'], 
    status_code=status.HTTP_200_OK, 
    description="descricao maneira"
)



