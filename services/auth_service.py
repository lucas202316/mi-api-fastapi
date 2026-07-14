from exceptions import UserAlreadyExistsError
from schemas import Usuario
from auth import hash_password
from repositories.user_repository import create_user

from repositories.user_repository import get_user_by_email
from auth import verify_password, create_access_token
from fastapi import HTTPException

from exceptions import AuthenticationError


def register(usuario: Usuario,
            db: sqlite3.Connection):

    password_hash = hash_password(usuario.password)

    return create_user(
    usuario,
    password_hash,
    db
)

def login(
    datos: Login,
    db: sqlite3.Connection
):
    usuario = get_user_by_email(
        db,
        datos.email
    )

    if not usuario:
        raise AuthenticationError()

    password_guardada = usuario["password"]

    if not verify_password(
    datos.password,
    password_guardada
):
        raise AuthenticationError()

    token = create_access_token(
        usuario["id"]
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }