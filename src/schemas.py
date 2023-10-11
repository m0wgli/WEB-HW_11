from pydantic import BaseModel
from datetime import date

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    
class ContactResponse(ContactBase):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    
    class Config:
        from_attributes = True