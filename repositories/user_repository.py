import sqlite3

from schemas import Usuario


def create_user(
    usuario: Usuario,
    password_hash: str,
    db: sqlite3.Connection
):
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

