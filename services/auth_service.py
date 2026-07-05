from exceptions import UserAlreadyExistsError
from schemas import Usuario
from auth import hash_password
from repositories.user_repository import create_user



def register_user(usuario, db):

    password_hash = hash_password(usuario.password)

    create_user(
        usuario,
        password_hash,
        db
    )


