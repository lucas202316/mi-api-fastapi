#guarda la información de la base de datos. Aquí se definen las funciones para conectarse a la base de datos y realizar operaciones CRUD (crear, leer, actualizar y eliminar) en la base de datos.
#Aquí vive toda la conexión con la base de datos.
#Si algún día cambias SQLite por MySQL o PostgreSQL, solamente modificarás este archivo.

import sqlite3

RUTA_DB = r"C:\Lucas\bbdd\mi_api.db"

conexion = sqlite3.connect(
    RUTA_DB,
    check_same_thread=False
)

cursor = conexion.cursor()
