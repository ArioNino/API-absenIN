from pydantic import BaseModel, field_validator
from typing import Optional


class UserBase(BaseModel):
    email: str  # Changed from EmailStr to str to allow .local domains
    name: str
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        """Basic email validation without strict domain checking"""
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None  # Changed from EmailStr to str
    name: Optional[str] = None
    password: Optional[str] = None
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        """Basic email validation without strict domain checking"""
        if v and '@' not in v:
            raise ValueError('Invalid email format')
        return v


class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
