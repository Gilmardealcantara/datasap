from sqlalchemy import Column, Integer, String, Date
from app import db


class Player(db.Model):
    __tablename__ = 'Player'

    id = Column(Integer, primary_key=True)  
    player_api_id = Column(Integer)   
    player_name = Column(String) 
    player_fifa_api_id = Column(Integer)  
    birthday = Column(Date)    
    height = Column(Integer)  
    weight = Column(Integer)

    def string_date(self):
        return str(self.birthday.day) + "/" + str(self.birthday.month)+ "/" + str(self.birthday.year)

    def __iter__(self):
        yield 'id', self.id
        yield 'player_api_id', self.player_api_id
        yield 'player_name', self.player_name
        yield 'player_fifa_api_id', self.player_fifa_api_id
        yield 'birthday', self.string_date()
        yield 'height', self.height
        yield 'weight', self.weight        
