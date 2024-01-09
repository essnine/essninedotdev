from sqlalchemy import ForeignKey, String, Integer, Text, DateTime, Boolean
from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column(String(60))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[str] = mapped_column(DateTime, nullable=False)
    author: Mapped[int] = mapped_column(ForeignKey("user.id"))
    active: Mapped[bool] = mapped_column(Boolean, default=1)
