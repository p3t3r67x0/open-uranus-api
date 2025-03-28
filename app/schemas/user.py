from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

from app.models.user import UserBase
from app.services.auth import validate_password


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    i18n_locale_id: Optional[int] = None

    @field_validator('password')
    def validate_user_password(cls, password):
        return validate_password(password)

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: EmailStr
    password: str

    @field_validator('password')
    def validate_user_password(cls, password):
        return validate_password(password)


class UserRead(UserBase):
    id: int


class UserSignin(BaseModel):
    username: EmailStr
    password: str


class UserResponse(BaseModel):
    user_id: int
    user_email_address: str
    user_display_name: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshToken(BaseModel):
    refresh_token: str


class PasswordChangeRequest(BaseModel):
    reset_token: str
    new_password: str


class UserRoleResponse(BaseModel):
    organizer_name: str
    role_organization: bool
    role_venue: bool
    role_space: bool
    role_event: bool
