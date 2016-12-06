from sqlalchemy import Column, Integer, String, Date
from app import db


class Team(db.Model):
    __tablename__ = 'Team'

    id = Column(Integer, primary_key=True)
    team_api_id = Column(Integer)
    team_fifa_api_id = Column(Integer)
    team_long_name = Column(String)
    team_short_name = Column(String)

    def __iter__(self):
        yield 'id', self.id
        yield 'team_api_id', self.team_api_id
        yield 'team_fifa_api_id', self.team_fifa_api_id
        yield 'team_long_name', self.team_long_name
        yield 'team_short_name', self.team_short_name
