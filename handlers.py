# este es un ejemplo de cómo manejar excepciones personalizadas en FastAPI
from fastapi import Request #Representa la petición HTTP que llegó al servidor.
from fastapi.responses import JSONResponse 
from exceptions import UserNotFoundError


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
