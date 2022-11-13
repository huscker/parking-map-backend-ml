from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from app.views.auth import Token, UserInfo, UserLogin, UserIn
from app.services.keycloak_driver import KeycloakDriver

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(tags=["User authentication"])

@router.get('/user')
async def get_user_info(token: str = Depends(oauth2_scheme)) -> UserInfo:
    userinfo = await KeycloakDriver.get_user_info(Token(access_token=token))
    return UserInfo(**userinfo)

@router.post('/register')
async def register_user(user: UserIn) -> None:
    await KeycloakDriver.register_user(user)

@router.post('/login')
async def login_user(user: UserLogin) -> Token:
    token = await KeycloakDriver.get_access_token(user)
    return token