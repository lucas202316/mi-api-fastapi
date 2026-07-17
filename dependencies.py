#FastAPI utiliza mucho las dependencias.
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import sqlite3
from database import get_db
from repositories.user_repository import get_user_by_id

from auth import (
    decode_access_token
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

#en la version original era una funcion auxiliar para obtener el usuario actual a partir del token
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: sqlite3.Connection = Depends(get_db)
):
    try:

        payload = decode_access_token(token)

        user_id = payload.get("sub")
        rol = payload.get("rol")

        if user_id is None or rol is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

        try:
            user_id = int(user_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

        usuario = get_user_by_id(
            db,
            user_id
        )

        if usuario is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario no encontrado"
            )

        return usuario

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudo validar el token"
        )
