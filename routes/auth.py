#endpoint de login
from fastapi import APIRouter

from schemas import Login
from database import cursor
from auth import (
    verify_password,
    create_access_token
)

router = APIRouter()


#login de usuario
@router.post("/login")
def login(datos: Login):

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ?",
        (datos.email,)
    )

    usuario = cursor.fetchone()
    if usuario is None:
        return {
            "error": "Correo o contraseña incorrectos."
        }
    password_guardada = usuario[3] 
    
    if verify_password(
        datos.password,
        password_guardada
    ):

        token = create_access_token(usuario[0])    
        
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
