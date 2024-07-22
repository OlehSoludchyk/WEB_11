from datetime import date

from typing import Optional
from pydantic import BaseModel, Field, EmailStr



class ContactSchema(BaseModel):
    firstname: str 
    surname: str 
    email: EmailStr
    phone: str
    birthday: date
    details: str | None = None


class ContactUpdateSchema(ContactSchema):
    firstname: Optional[str] = Field(None, min_length=3, max_length=25)
    surname: Optional[str] = Field(None, min_length=3, max_length=25)
    email: Optional[EmailStr] = Field(None, min_length=10, max_length=50)
    phone: Optional[str] = Field(None, min_length=5, max_length=20)
    birthday: date
    details: Optional[str] = Field(None, max_length=150)


class ContactResponse(BaseModel):
    firstname: str 
    surname: str 
    email: EmailStr 
    phone: str 
    birthday: date 
    details: str

    class Config:
        orm_mode = True