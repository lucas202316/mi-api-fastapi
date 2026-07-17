
import sqlite3

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

from exceptions import AuthenticationError

from repositories.user_repository import (
    create_user,
    get_user_by_email
)

from schemas import Usuario, Login

def register_user(usuario: Usuario,
            db: sqlite3.Connection):

    password_hash = hash_password(usuario.password)
    rol = "user"

    return create_user(
    usuario,
    password_hash,
    rol,
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
        usuario["id"],
        usuario["rol"]
)


    return {
        "access_token": token,
        "token_type": "bearer"
    }