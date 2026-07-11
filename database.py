#guarda la información de la base de datos. Aquí se definen las funciones para conectarse a la base de datos y realizar operaciones CRUD (crear, leer, actualizar y eliminar) en la base de datos.
#Aquí vive toda la conexión con la base de datos.
#Si algún día cambias SQLite por MySQL o PostgreSQL, solamente modificarás este archivo.

import sqlite3

from config import DATABASE_PATH


def get_db():

    conexion = sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False
    )

    conexion.row_factory = sqlite3.Row #sirve para que el cursor devuelva diccionarios en lugar de tuplas. Así podemos acceder a los datos por nombre de columna en lugar de por índice.

    try:
        yield conexion

    finally:#se ejecuta al terminar la conexión con la base de datos pase lo que pase. Se ejecuta siempre.
        conexion.close()

