#maneja los endpoints de registro de usuarios. Aquí se definen las rutas y la lógica para registrar nuevos usuarios en la aplicación.
#Aquí van los endpoints de registro

from fastapi import APIRouter, Depends
from services.auth_service import register_user
from schemas import Usuario
from database import get_db
import sqlite3
from exceptions import UserAlreadyExistsError

from dependencies import get_current_user
from auth import hash_password

router = APIRouter()

#registro de usuario
@router.post("/register")
def register(
    usuario: Usuario,
    db: sqlite3.Connection = Depends(get_db)
):

    try:

        register_user(
            usuario,
            db
        )

        return {
            "mensaje": "Usuario registrado"
        }

    except UserAlreadyExistsError:

        return {
            "mensaje": "El correo electrónico ya está registrado"
        }



#rura protegida que requiere autenticación
@router.get("/profile")
def profile(usuario = Depends(get_current_user)):
    return {"mensaje": f"Bienvenido, usuario con ID {usuario['id']}"}

#solicitudes
#registro de usuario
'''{
    "nombre":"Juan",
    "email":"juan@gmail.com",
    "password":"123456"
}'''