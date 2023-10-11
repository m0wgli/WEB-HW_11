from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactBase, ContactResponse
from src.database.models import Contact
from src.repository import contacts as repository_contacts


router = APIRouter(prefix="/contacts", tags=["Contacts"])



@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_new_contact(body: ContactBase, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(body, db)


@router.get("/all", response_model=List[ContactResponse])
async def read_all_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip, limit, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact_by_id(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactBase, contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.delete("/remove/{contact_id}", response_model=ContactResponse)
async def remove_user(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.get("/find/{query}", response_model=List[ContactResponse])
async def find_contacts(query: str, db: Session = Depends(get_db)):
    contacts = await repository_contacts.search_contacts(query, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    return contacts


@router.get("/birthday/{days}", response_model=List[ContactResponse])
async def contacts_birthday(days: int, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_birthday_per_week(days, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    return contacts