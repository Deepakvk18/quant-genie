from fastapi import APIRouter, Depends, Response, Security
from database.user import UserRepo
from schema.user import UserCreate, UserCreateResponse, UserPatch, LoginResponse
from models.user import UserModel
from exceptions import QuantGenieException
from schema.user import UserCreateResponse
from utils import get_settings, PasswordHasher
from fastapi_jwt import JwtAccessCookie, JwtAuthorizationCredentials, JwtRefreshCookie
from datetime import timedelta


settings = get_settings()
access_security = JwtAccessCookie(secret_key=settings.SECRET_KEY, auto_error=True, access_expires_delta=timedelta(seconds=settings.ACCESS_EXPIRY))
refresh_security = JwtRefreshCookie(secret_key=settings.SECRET_KEY, auto_error=True, refresh_expires_delta=timedelta(seconds=settings.REFRESH_EXPIRY))

user_router = APIRouter(tags=["user"])

@user_router.post('/signup', response_model=UserCreateResponse)
async def get_user(new_user:UserCreate, credentials: JwtAuthorizationCredentials = Security(refresh_security), user: UserRepo = Depends(), hasher: PasswordHasher = Depends()):
    new_user.password = hasher.get_password_hash(new_user.password)
    created_user = user.create_user(new_user)
    return { 'message': 'User created successfully', 'user_id': str(created_user) }

@user_router.patch('/patch-api-keys/{user_id}', response_model=UserModel)
async def patch_api_keys(user_id: str, partial_user: UserPatch, credentials: JwtAuthorizationCredentials = Security(refresh_security), user: UserRepo = Depends()):
    updated_user = user.patch_user(partial_user, user_id)
    updated_user['_id'] = str(updated_user['_id'])
    return updated_user

@user_router.post('/login', response_model=LoginResponse)
async def login(login_user:UserCreate, response: Response, user: UserRepo = Depends(), hasher: PasswordHasher = Depends()):
    attempted_user = user.get_user_by_email(login_user.email)
    if not attempted_user:
        raise QuantGenieException(f'User with email {attempted_user.email} does not exist')
    if not (hasher.verify_password(login_user.password, attempted_user.get('password'))):
        raise QuantGenieException('Invalid Password')
    access_token = access_security.create_access_token(subject={'email': attempted_user.get('email')})
    refresh_token = refresh_security.create_refresh_token(subject={'email': attempted_user.get('email')})
    refresh_security.set_refresh_cookie(response=response, refresh_token=refresh_token, expires_delta=timedelta(seconds=settings.REFRESH_EXPIRY))
    access_security.set_access_cookie(response=response, access_token=access_token, expires_delta=timedelta(seconds=settings.ACCESS_EXPIRY))
    attempted_user['_id'] = str(attempted_user['_id'])
    return {'access_token': access_token, 'user': attempted_user}

@user_router.post('/refresh', response_model=LoginResponse)
async def refresh(response: Response, credentials: JwtAuthorizationCredentials = Security(refresh_security), user: UserRepo = Depends()):
    access_token = access_security.create_access_token(subject=credentials.subject)
    refresh_token = access_security.create_refresh_token(subject=credentials.subject)
    refresh_security.set_refresh_cookie(response=response, refresh_token=refresh_token, expires_delta=timedelta(seconds=settings.REFRESH_EXPIRY))
    access_security.set_access_cookie(response=response, access_token=access_token, expires_delta=timedelta(seconds=settings.ACCESS_EXPIRY))
    email = credentials.subject.get('email')
    login_user = user.get_user_by_email(email)
    login_user['_id'] = str(login_user['_id'])
    return {"access_token": access_token, 'user': login_user}