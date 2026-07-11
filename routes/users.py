#maneja los endpoints de registro de usuarios. Aquí se definen las rutas y la lógica para registrar nuevos usuarios en la aplicación.
#Aquí van los endpoints de registro



from fastapi import APIRouter, Depends, status
from services.auth_service import register_user
from schemas import MessageResponse, Usuario, UsuarioResponse, UsuarioUpdate

from database import get_db
import sqlite3
from exceptions import UserAlreadyExistsError

from dependencies import get_current_user
from auth import hash_password
from services import user_service

router = APIRouter()

#Ahora agregamos el nuevo endpoint.
@router.get("/users",response_model=list[UsuarioResponse])
def get_users(
    db: sqlite3.Connection = Depends(get_db)
):
    return user_service.get_all_users(db)

#Ahora agregamos el nuevo endpoint.
@router.get("/users/{user_id}",response_model=UsuarioResponse)
def get_user_by_id(
    user_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
    
        return user_service.get_user_by_id(db, user_id)

    

@router.put(
    "/users/{user_id}",
    response_model=UsuarioResponse
)
def update_user(
    user_id: int,
    datos: UsuarioUpdate,
    db: sqlite3.Connection = Depends(get_db)
):
   
        return user_service.update_user(
            db=db,
            user_id=user_id,
            nombre=datos.nombre,
            email=datos.email
        )

   
@router.delete("/users/{user_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
   
        user_service.delete_user(
            db=db,
            user_id=user_id
        )
        

   


#registro de usuario
@router.post("/register",
             response_model=MessageResponse,
             status_code=status.HTTP_201_CREATED)
def register(
    usuario: Usuario,
    db: sqlite3.Connection = Depends(get_db)
):

  

        register_user(
            usuario,
            db
        )

        return {
            "mensaje": "Usuario registrado"
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