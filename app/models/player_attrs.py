from sqlalchemy import Column, Integer, String, Date
from app import db


class PlayerAttr(db.Model):
    __tablename__ = 'Player_Attributes'


    id = Column(Integer, primary_key=True)
    player_fifa_api_id = Column(Integer)
    player_api_id = Column(Integer)
    date = Column(Date)
    overall_rating = Column(Integer)
    potential = Column(Integer)
    preferred_foot = Column(String)
    attacking_work_rate = Column(String)
    defensive_work_rate = Column(String)
    crossing = Column(Integer)
    finishing = Column(Integer)
    heading_accuracy = Column(Integer)
    short_passing = Column(Integer)
    volleys = Column(Integer)
    dribbling = Column(Integer)
    curve = Column(Integer)
    free_kick_accuracy = Column(Integer)
    long_passing = Column(Integer)
    ball_control = Column(Integer)
    acceleration = Column(Integer)
    sprint_speed = Column(Integer)
    agility = Column(Integer)
    reactions = Column(Integer)
    balance = Column(Integer)
    shot_power = Column(Integer)
    jumping = Column(Integer)
    stamina = Column(Integer)
    strength = Column(Integer)
    long_shots = Column(Integer)
    aggression = Column(Integer)
    interceptions = Column(Integer)
    positioning = Column(Integer)
    vision = Column(Integer)
    penalties = Column(Integer)
    marking = Column(Integer)
    standing_tackle = Column(Integer)
    sliding_tackle = Column(Integer)
    gk_diving = Column(Integer)
    gk_handling = Column(Integer)
    gk_kicking = Column(Integer)
    gk_positioning = Column(Integer)
    gk_reflexes = Column(Integer)

    def string_date(self):
        return str(self.date.day) + "/" + str(self.date.month)+ "/" + str(self.date.year)

    def __iter__(self):
        yield 'id', self.id
        yield 'player_fifa_api_id', self.player_fifa_api_id
        yield 'player_api_id', self.player_api_id
        yield 'date', self.string_date()
        yield 'overall_rating', self.overall_rating
        yield 'potential', self.potential
        yield 'preferred_foot', self.preferred_foot
        yield 'attacking_work_rate', self.attacking_work_rate
        yield 'defensive_work_rate', self.defensive_work_rate
        yield 'crossing', self.crossing
        yield 'finishing', self.finishing
        yield 'heading_accuracy', self.heading_accuracy
        yield 'short_passing', self.short_passing
        yield 'volleys', self.volleys
        yield 'dribbling', self.dribbling
        yield 'curve', self.curve
        yield 'free_kick_accuracy', self.free_kick_accuracy
        yield 'long_passing', self.long_passing
        yield 'ball_control', self.ball_control
        yield 'acceleration', self.acceleration
        yield 'sprint_speed', self.sprint_speed
        yield 'agility', self.agility
        yield 'reactions', self.reactions
        yield 'balance', self.balance
        yield 'shot_power', self.shot_power
        yield 'jumping', self.jumping
        yield 'stamina', self.stamina
        yield 'strength', self.strength
        yield 'long_shots', self.long_shots
        yield 'aggression', self.aggression
        yield 'interceptions', self.interceptions
        yield 'positioning', self.positioning
        yield 'vision', self.vision
        yield 'penalties', self.penalties
        yield 'marking', self.marking
        yield 'standing_tackle', self.standing_tackle
        yield 'sliding_tackle', self.sliding_tackle
        yield 'gk_diving', self.gk_diving
        yield 'gk_handling', self.gk_handling
        yield 'gk_kicking', self.gk_kicking
        yield 'gk_positioning', self.gk_positioning
        yield 'gk_reflexes', self.gk_reflexes
