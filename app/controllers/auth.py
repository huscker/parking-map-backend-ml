from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.views.auth import Token, UserInfo, UserLogin, UserIn, TokenOut
from app.services.keycloak_driver import KeycloakDriver

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(tags=["User authentication"])

@router.get('/user')
async def get_user_info(token: str = Depends(oauth2_scheme)) -> UserInfo:
    userinfo = await KeycloakDriver.get_user_info(Token(access_token=token))
    return userinfo

@router.post('/register')
async def register_user(user: UserIn) -> None:
    await KeycloakDriver.register_user(user)

@router.post('/login', response_model=TokenOut)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    token = await KeycloakDriver.get_access_token(UserLogin(
        username=form_data.username,
        password=form_data.password
    ))
    return token