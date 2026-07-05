#maneja los endpoints de registro de usuarios. Aquí se definen las rutas y la lógica para registrar nuevos usuarios en la aplicación.
#Aquí van los endpoints de registro

from fastapi import HTTPException
from exceptions import UserNotFoundError

from fastapi import APIRouter, Depends
from services.auth_service import register_user
from schemas import Usuario
from schemas import UserUpdate
from database import get_db
import sqlite3
from exceptions import UserAlreadyExistsError

from dependencies import get_current_user
from auth import hash_password
from services import user_service

router = APIRouter()

#Ahora agregamos el nuevo endpoint.
@router.get("/users")
def get_users(
    db: sqlite3.Connection = Depends(get_db)
):
    return user_service.get_all_users(db)

#Ahora agregamos el nuevo endpoint.
@router.get("/users/{user_id}")
def get_user_by_id(
    user_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
    try:
        return user_service.get_user_by_id(db, user_id)

    except UserNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    datos: UserUpdate,
    db: sqlite3.Connection = Depends(get_db)
):
    try:
        user_service.update_user(
            db=db,
            user_id=user_id,
            nombre=datos.nombre,
            email=datos.email
        )

        return {
            "message": "Usuario actualizado correctamente"
        }

    except UserNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
    try:
        user_service.delete_user(
            db=db,
            user_id=user_id
        )

        return {
            "message": "Usuario eliminado correctamente"
        }

    except UserNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )



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