#maneja los endpoints de registro de usuarios. Aquí se definen las rutas y la lógica para registrar nuevos usuarios en la aplicación.
#Aquí van los endpoints de registro

from fastapi import APIRouter, Depends

from schemas import Usuario
from database import conexion, cursor
from dependencies import get_current_user
from auth import hash_password

router = APIRouter()

#registro de usuario
@router.post("/register")
def register(usuario: Usuario):

    password_hash = hash_password(usuario.password)
    
    try:
        cursor.execute(
            """
            INSERT INTO usuarios(nombre, email, password)
            VALUES (?, ?, ?)
            """,
            (
                usuario.nombre,
                usuario.email,
                password_hash
            )
        )

        conexion.commit()
        return {
        "mensaje": "Usuario registrado",
        "password_original": usuario.password,
        "password_hasheada": password_hash
    }
    except sqlite3.IntegrityError:
        return {"mensaje": "El correo electrónico ya está registrado"}

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