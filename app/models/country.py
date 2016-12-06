from sqlalchemy import Column, Integer, String
from app import db


class Country(db.Model):
    __tablename__ = 'Country'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name