import sqlite3
from schemas import Usuario
from auth import hash_password
from repositories.user_repository import create_user



def register_user(
    usuario: Usuario,
    db: sqlite3.Connection
):

    password_hash = hash_password(usuario.password)

    try:
        create_user(
        usuario,
        password_hash,
        db
    )


        return {
            "mensaje": "Usuario registrado",
            "password_original": usuario.password,
            "password_hasheada": password_hash
        }

    except sqlite3.IntegrityError:
        return {
            "mensaje": "El correo electrónico ya está registrado"
        }

