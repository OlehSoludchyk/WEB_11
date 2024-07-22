from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(25), index=True)
    surname: Mapped[str] = mapped_column(String(25), index=True)
    email: Mapped[str] = mapped_column(String(50), index=True)
    phone: Mapped[str] = mapped_column(String(20), index=True)
    birthday: Mapped[Date] = mapped_column(Date)
    details: Mapped[str | None] = mapped_column(String(150), nullable=True)