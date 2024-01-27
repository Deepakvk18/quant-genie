from fastapi import APIRouter, Depends, Response, Security
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials, JwtRefreshBearer
from datetime import timedelta
from utils import get_settings

settings = get_settings()

access_security = JwtAccessBearer(secret_key=settings.SECRET_KEY, auto_error=True, access_expires_delta=timedelta(seconds=settings.ACCESS_EXPIRY))
refresh_security = JwtRefreshBearer(secret_key=settings.SECRET_KEY, auto_error=True, refresh_expires_delta=timedelta(seconds=settings.REFRESH_EXPIRY))