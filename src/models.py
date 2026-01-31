from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            
        }

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    quote: Mapped[str] = mapped_column(String(120),nullable=False)
    image: Mapped[str] = mapped_column(String(120),nullable=False)
    job: Mapped[str] = mapped_column(String(120),nullable=False)
    age: Mapped[str] = mapped_column(String(120),nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "quote": self.quote,
            "image": self.image,
            "job": self.job,
            "age": self.age
        }