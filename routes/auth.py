#endpoint de login
from fastapi import APIRouter

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
def login(datos: Login,
          db: sqlite3.Connection = Depends(get_db)):

    cursor = db.cursor() #se crea dentro de la función para que se cierre automáticamente al finalizar la función, evitando problemas de conexión abierta
    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ?",
        (datos.email,)
    )

    usuario = cursor.fetchone()
    if usuario is None:
        return {
            "error": "Correo o contraseña incorrectos."
        }
    password_guardada = usuario["password"]
    
    if verify_password(
        datos.password,
        password_guardada
    ):

        token = create_access_token(usuario["id"])    
        
        '''datos_token = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

        print(datos_token)''' #solo para comprobar que el token se decodifica correctamente y se obtiene el id del usuario

        return {
            "access_token": token #lo que devuelve POST /login
        }
            

    return {
        "error": "Correo o contraseña incorrectos."
    }
    
#login de usuario
'''{
    "email": "juan@gmail.com",
    "password": "123456"
}'''
