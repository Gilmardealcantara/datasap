from sqlalchemy import Column, Integer, String
from app import db


class League(db.Model):
    __tablename__ = 'League'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer)
    name = Column(String)

    def __iter__(self):
        yield 'id', self.id
        yield 'country_id', self.country_id
        yield 'name', self.name