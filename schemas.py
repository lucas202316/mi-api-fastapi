#valida los datos de entrada y salida de la API. Aquí se definen los modelos de datos que se utilizan para validar las solicitudes y respuestas de la API.
#Aquí viven los modelos de Pydantic.
#Todos los esquemas de entrada y salida estarán organizados en un solo lugar.

from pydantic import BaseModel

#modelos de datos pydantic
#clase base para los modelos de usuario
class UsuarioBase(BaseModel):
    nombre: str
    email: str


class Usuario(UsuarioBase):
    password: str


class UsuarioUpdate(UsuarioBase):
    pass


class Login(BaseModel):
   email: str
   password: str
   

