#endpoint de login
from fastapi import APIRouter
from services import auth_service
from schemas import Login, Token
from fastapi import Depends
import sqlite3
from database import get_db
from auth import (
    verify_password,
    create_access_token
)

router = APIRouter()


#login de usuario
@router.post("/login", response_model=Token)
def login(
    datos: Login,
    db: sqlite3.Connection = Depends(get_db)
):
    return auth_service.login(
        datos,
        db
    )


    
#login de usuario
'''{
    "email": "juan@gmail.com",
    "password": "123456"
}'''
