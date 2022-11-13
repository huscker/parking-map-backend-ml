from pydantic import BaseModel, Field
from typing import Optional

class Token(BaseModel):
    access_token: str
    refresh_token: Optional[str]
    expires_in: Optional[int]
    refresh_expires_in: Optional[int]
    token_type: Optional[str]

class TokenOut(BaseModel):
    access_token: str
    token_type: str

class UserIn(BaseModel):
    name: str
    given_name: str
    family_name: str
    preferred_username: str
    email: str
    password: str

class UserInfo(UserIn):
    email_verified: bool
    password: Optional[str] = ''

class UserLogin(BaseModel):
    username: str
    password: str