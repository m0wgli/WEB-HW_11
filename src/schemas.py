from datetime import date
from pydantic import BaseModel


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date


class ContactResponse(ContactBase):
    first_name: str = "Jonh"
    last_name: str = "Wick"
    email: str = "JW@continental.com"
    phone_number: str = "4124478554"
    birthday: date = date(year=1983, month=10, day=14)

    class Config:
        from_attributes = True
