from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, EmailStr
from database.model.User import UserModel
from database.config.database import session
from typing import Optional

user_router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None 
    hashed_password: Optional[str] = None


@user_router.get('/users', description="listar usuários")
def list_users() -> None:
    return session.query(UserModel).all()

@user_router.get('/users/{user_id}', description="visualizar um usuário")
def list_users(user_id: int) -> None:
    return session.query(UserModel).filter(UserModel.id==user_id).first()

@user_router.post('/users', status_code=status.HTTP_201_CREATED, description='adicionar usuário')
def create_user(user: UserCreate):
    db_user = session.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado.")

    new_user = UserModel(
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password,
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@user_router.delete('/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT, description='Deletar usuário')
def delete_user(user_id: int ):
    db_user = session.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")
    
    session.delete(db_user)
    session.commit()
    
    return None


@user_router.put('/users/{user_id}', status_code=status.HTTP_200_OK)
def update_user(user_id, updates: UserUpdate):
    
    try:
        user = session.query(UserModel).filter(UserModel.id == user_id).first()
        
        if user:
            # Atualizar os atributos com os novos valores
            for key, value in updates:
                if(value == None):
                    continue
                setattr(user, key, value)

            # Persistir as alterações
            session.commit()
            print("Usuário atualizado com sucesso.")
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "hashed_password": user.hashed_password,
                "is_admin": user.is_admin,
                "is_active": user.is_active
            }
        else:
            print("Usuário não encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print(updates)
        session.rollback()  # Reverter a sessão em caso de erro
    finally:
        session.close()  # Fechar a sessão
