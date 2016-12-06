from sqlalchemy import Column, Integer, String
from app import db


class SqliteSequence(db.Model):
    __tablename__ = 'sqlite_sequence'

    name = Column(String, primary_key=True)
    seq = Column(Integer)

    def __iter__(self):
        yield 'name', self.name
        yield 'seq', self.seq