from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas.contact import ContactSchema, ContactUpdateSchema


async def get_contacts(limit: int, offset: int, db: Session):
    statmnt = select(Contact).offset(offset).limit(limit)
    contacts = await db.execute(statmnt)
    return contacts.scalars().all()


async def get_contact(contact_id: int, db: Session):
    statmnt = select(Contact).filter_by(id=contact_id)
    contact = await db.execute(statmnt)
    return contact.scalar_one_or_none()


async def create_contact(body: ContactSchema, db: Session):
    contact = Contact(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh()
    return contact


async def update_contact(contact_id: int, body: ContactUpdateSchema, db: Session):
    statmnt = select(Contact).filter_by(id=contact_id)
    result = await db.execute(statmnt)
    contact = result.scalar_one_or_none()
    if contact:
        contact.firstname = body.firstname
        contact.surname = body.surname
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.details = body.details
        await db.commit()
        await db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: Session):
    statmnt = select(Contact).filter_by(id=contact_id)
    contact = db.execute(statmnt)
    contact = contact.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact