import sqlite3

from repositories import user_repository
from exceptions import UserNotFoundError

def get_all_users(db: sqlite3.Connection):
    return user_repository.get_all_users(db)

def get_user_by_id(db: sqlite3.Connection, user_id: int):
    usuario = user_repository.get_user_by_id(db, user_id)

    if usuario is None:
        raise UserNotFoundError()

    return usuario
