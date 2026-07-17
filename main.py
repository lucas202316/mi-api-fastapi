#recibe la aplicación de FastAPI y registra las rutas. También importa desde routes y dependencies, que son los archivos donde se encuentra la lógica de negocio y las dependencias de FastAPI.
#Aquí casi nunca se escribe lógica de negocio. Su función es crear la aplicación de FastAPI y #registrar las rutas.
#tambien importa desde routes y dependencies, que son los archivos donde se encuentra la lógica de negocio y las dependencias de FastAPI.

#importaciones
from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.users import router as users_router
from handlers import user_already_exists_handler
from handlers import (
    user_not_found_handler,
    user_already_exists_handler,
    authentication_error_handler
)
from exceptions import UserNotFoundError
from exceptions import UserAlreadyExistsError,  AuthenticationError

#constantes


app = FastAPI()#objeto de la clase FastAPI, que representa la aplicación web y se utiliza para definir rutas, manejar solicitudes y respuestas, y configurar la aplicación.

#registrar el manejador de excepciones personalizado para UserNotFoundError
app.add_exception_handler(
    UserNotFoundError,
    user_not_found_handler
)
app.add_exception_handler(
    UserAlreadyExistsError,
    user_already_exists_handler
)

app.add_exception_handler(
    AuthenticationError,
    authentication_error_handler
)


#registra las rutas de autenticación y usuarios en la aplicación FastAPI
##Se registra el router de autenticación en la aplicación FastAPI. Esto permite que las rutas definidas en auth_router estén disponibles en la aplicación principal.
app.include_router(auth_router)
app.include_router(users_router)

#endpoints
#inicio de la API
@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}






