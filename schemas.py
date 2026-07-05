#valida los datos de entrada y salida de la API. Aquí se definen los modelos de datos que se utilizan para validar las solicitudes y respuestas de la API.
#Aquí viven los modelos de Pydantic.
#Todos los esquemas de entrada y salida estarán organizados en un solo lugar.

from pydantic import BaseModel

#modelos de datos pydantic
class Usuario(BaseModel):
    nombre: str
    email: str
    password: str

class Login(BaseModel):
   email: str
   password: str
   
class UserUpdate(BaseModel):
    nombre: str
    email: str
