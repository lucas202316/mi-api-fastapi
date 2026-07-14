# este es un ejemplo de cómo manejar excepciones personalizadas en FastAPI
from fastapi import Request #Representa la petición HTTP que llegó al servidor.
from fastapi.responses import JSONResponse 

from exceptions import (UserNotFoundError,
                        UserAlreadyExistsError,
                        AuthenticationError
                        )

def user_not_found_handler(
    request: Request,
    exc: UserNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Usuario no encontrado"
        }
    )

def user_already_exists_handler(
    request: Request,
    exc: UserAlreadyExistsError
):
    return JSONResponse(
        status_code=409,
        content={
            "detail": "El correo electrónico ya está registrado"
        }
    )

def authentication_error_handler(
    request: Request,
    exc: AuthenticationError
):
    return JSONResponse(
        status_code=401,
        content={
            "detail": "Correo o contraseña incorrectos."
        }
    )