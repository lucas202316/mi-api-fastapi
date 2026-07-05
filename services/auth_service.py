import sqlite3
from schemas import Usuario
from auth import hash_password


def register_user(
    usuario: Usuario,
    db: sqlite3.Connection
):

    password_hash = hash_password(usuario.password)

    try:
        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO usuarios(nombre, email, password)
            VALUES (?, ?, ?)
            """,
            (
                usuario.nombre,
                usuario.email,
                password_hash
            )
        )

        db.commit()

        return {
            "mensaje": "Usuario registrado",
            "password_original": usuario.password,
            "password_hasheada": password_hash
        }

    except sqlite3.IntegrityError:
        return {
            "mensaje": "El correo electrónico ya está registrado"
        }

