from sqlalchemy import Column, Integer, String, Date
from app import db


class TeamAttr(db.Model):
    __tablename__ = 'Team_Attributes'

    id = Column(Integer, primary_key=True)
    team_fifa_api_id = Column(Integer) #    434
    team_api_id = Column(Integer) #     9930
    date = Column(Date) #    2010-
    buildUpPlaySpeed = Column(Integer) #    60
    buildUpPlaySpeedClass = Column(String) #   Balanced
    buildUpPlayDribbling = Column(Integer) #    3
    buildUpPlayDribblingClass = Column(String) #   Little
    buildUpPlayPassing = Column(Integer) #  50
    buildUpPlayPassingClass = Column(String) #     Mixed
    buildUpPlayPositioningClass = Column(String) #     Organised
    chanceCreationPassing = Column(Integer) #   60
    chanceCreationPassingClass = Column(String) #  Normal
    chanceCreationCrossing = Column(Integer) #  65
    chanceCreationCrossingClass = Column(String) #     Normal
    chanceCreationShooting = Column(Integer) #  55
    chanceCreationShootingClass = Column(String) #     Normal
    chanceCreationPositioningClass = Column(String) #  Organised
    defencePressure = Column(Integer) #     50
    defencePressureClass = Column(String) #    Medium
    defenceAggression = Column(Integer) #   55
    defenceAggressionClass = Column(String) #  Press
    defenceTeamWidth = Column(Integer) #    45
    defenceTeamWidthClass = Column(String) #   Normal
    defenceDefenderLineClass = Column(String) #    Cover


    def string_date(self):
        return str(self.date.day) + "/" + str(self.date.month)+ "/" + str(self.date.year)


    def __iter__(self):
        yield 'team_fifa_api_id', self.team_fifa_api_id 
        yield 'team_api_id', self.team_api_id 
        yield 'date', self.string_date() 
        yield 'buildUpPlaySpeed', self.buildUpPlaySpeed 
        yield 'buildUpPlaySpeedClass', self.buildUpPlaySpeedClass 
        yield 'buildUpPlayDribbling', self.buildUpPlayDribbling 
        yield 'buildUpPlayDribblingClass', self.buildUpPlayDribblingClass 
        yield 'buildUpPlayPassing', self.buildUpPlayPassing 
        yield 'buildUpPlayPassingClass', self.buildUpPlayPassingClass 
        yield 'buildUpPlayPositioningClass', self.buildUpPlayPositioningClass 
        yield 'chanceCreationPassing', self.chanceCreationPassing 
        yield 'chanceCreationPassingClass', self.chanceCreationPassingClass 
        yield 'chanceCreationCrossing', self.chanceCreationCrossing 
        yield 'chanceCreationCrossingClass', self.chanceCreationCrossingClass 
        yield 'chanceCreationShooting', self.chanceCreationShooting 
        yield 'chanceCreationShootingClass', self.chanceCreationShootingClass 
        yield 'chanceCreationPositioningClass', self.chanceCreationPositioningClass 
        yield 'defencePressure', self.defencePressure 
        yield 'defencePressureClass', self.defencePressureClass 
        yield 'defenceAggression', self.defenceAggression 
        yield 'defenceAggressionClass', self.defenceAggressionClass 
        yield 'defenceTeamWidth', self.defenceTeamWidth 
        yield 'defenceTeamWidthClass', self.defenceTeamWidthClass 
        yield 'defenceDefenderLineClass', self.defenceDefenderLineClass 
