import json

from app.settings import KEYCLOAK_PORT, KEYCLOAK_URL, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, REALM_NAME, \
    KEYCLOAK_ADMIN_USER, KEYCLOAK_ADMIN_PASSWORD
from keycloak import KeycloakAdmin, KeycloakOpenID
from aiohttp import ClientSession
from app.views.auth import Token, UserInfo, UserLogin, UserIn


class KeycloakDriver:
    client_regular = KeycloakOpenID(
        server_url=KEYCLOAK_URL,
        client_id=KEYCLOAK_CLIENT_ID,
        realm_name=REALM_NAME,
        client_secret_key=KEYCLOAK_CLIENT_SECRET)
    client_admin = KeycloakAdmin(
        server_url=KEYCLOAK_URL,
        username=KEYCLOAK_ADMIN_USER,
        password=KEYCLOAK_ADMIN_PASSWORD,
        realm_name=REALM_NAME,
        user_realm_name=REALM_NAME,
        client_secret_key=KEYCLOAK_CLIENT_SECRET,
        client_id=KEYCLOAK_CLIENT_ID,
        verify=True)

    @classmethod
    async def connect_client_admin(cls):
        await cls.client_admin.connect()
        # print(await cls.client_admin.users_count())

    @classmethod
    async def get_access_token(cls, user: UserLogin) -> Token:
        token = await cls.client_regular.token(user.username, user.password)
        return Token(**token)

    @classmethod
    async def refresh_token(cls, token: Token) -> Token:
        token = await cls.client_regular.refresh_token(token.refresh_token)
        return Token(**token)

    @classmethod
    async def user_logout(cls, token: Token) -> None:
        await cls.client_regular.logout(token.refresh_token)

    @classmethod
    async def get_user_info(cls, token: Token) -> UserInfo:
        userinfo = await cls.client_regular.userinfo(token.access_token)
        return UserInfo(**userinfo)

    @classmethod
    async def register_user(cls, user: UserIn) -> None:
        url = KEYCLOAK_URL + f"/admin/realms/{REALM_NAME}/users"
        data = {
            "firstName": user.given_name,
            "lastName": user.family_name,
            "email": user.email,
            "username": user.preferred_username
        }
        headers = {
            "Authorization": f"Bearer {cls.client_admin.token['access_token']}",
            "Content-Type": "application/json",
            'Accept': 'application/json'
        }
        async with ClientSession() as client:
            response = await client.post(
                url,
                data=json.dumps(data),
                headers=headers
            )
            print(response)
