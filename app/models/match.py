from sqlalchemy import Column, Integer, String, Date
from app import db


class Match(db.Model):
    __tablename__ = 'Match'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer)
    league_id = Column(Integer)
    season = Column(String)
    stage = Column(Integer)
    date = Column(Date)
    match_api_id = Column(Integer)
    home_team_api_id = Column(Integer)
    away_team_api_id = Column(Integer)
    home_team_goal = Column(Integer)
    away_team_goal = Column(Integer)
    home_player_X1 = Column(Integer)
    home_player_X2 = Column(Integer)
    home_player_X3 = Column(Integer)
    home_player_X4 = Column(Integer)
    home_player_X5 = Column(Integer)
    home_player_X6 = Column(Integer)
    home_player_X7 = Column(Integer)
    home_player_X8 = Column(Integer)
    home_player_X9 = Column(Integer)
    home_player_X10 = Column(Integer)
    home_player_X11 = Column(Integer)
    away_player_X1 = Column(Integer)
    away_player_X2 = Column(Integer)
    away_player_X3 = Column(Integer)
    away_player_X4 = Column(Integer)
    away_player_X5 = Column(Integer)
    away_player_X6 = Column(Integer)
    away_player_X7 = Column(Integer)
    away_player_X8 = Column(Integer)
    away_player_X9 = Column(Integer)
    away_player_X10 = Column(Integer)
    away_player_X11 = Column(Integer)
    home_player_Y1 = Column(Integer)
    home_player_Y2 = Column(Integer)
    home_player_Y3 = Column(Integer)
    home_player_Y4 = Column(Integer)
    home_player_Y5 = Column(Integer)
    home_player_Y6 = Column(Integer)
    home_player_Y7 = Column(Integer)
    home_player_Y8 = Column(Integer)
    home_player_Y9 = Column(Integer)
    home_player_Y10 = Column(Integer)
    home_player_Y11 = Column(Integer)
    away_player_Y1 = Column(Integer)
    away_player_Y2 = Column(Integer)
    away_player_Y3 = Column(Integer)
    away_player_Y4 = Column(Integer)
    away_player_Y5 = Column(Integer)
    away_player_Y6 = Column(Integer)
    away_player_Y7 = Column(Integer)
    away_player_Y8 = Column(Integer)
    away_player_Y9 = Column(Integer)
    away_player_Y10 = Column(Integer)
    away_player_Y11 = Column(Integer)
    home_player_1 = Column(Integer)
    home_player_2 = Column(Integer)
    home_player_3 = Column(Integer)
    home_player_4 = Column(Integer)
    home_player_5 = Column(Integer)
    home_player_6 = Column(Integer)
    home_player_7 = Column(Integer)
    home_player_8 = Column(Integer)
    home_player_9 = Column(Integer)
    home_player_10 = Column(Integer)
    home_player_11 = Column(Integer)
    away_player_1 = Column(Integer)
    away_player_2 = Column(Integer)
    away_player_3 = Column(Integer)
    away_player_4 = Column(Integer)
    away_player_5 = Column(Integer)
    away_player_6 = Column(Integer)
    away_player_7 = Column(Integer)
    away_player_8 = Column(Integer)
    away_player_9 = Column(Integer)
    away_player_10 = Column(Integer)
    away_player_11 = Column(Integer)
    goal = Column(Integer)
    shoton = Column(Integer)
    shotoff = Column(Integer)
    foulcommit = Column(Integer)
    card = Column(Integer)
    cross = Column(Integer)
    corner = Column(Integer)
    possession = Column(Integer)
    B365H = Column(Integer)
    B365D = Column(Integer)
    B365A = Column(Integer)
    BWH = Column(Integer)
    BWD = Column(Integer)
    BWA = Column(Integer)
    IWH = Column(Integer)
    IWD = Column(Integer)
    IWA = Column(Integer)
    LBH = Column(Integer)
    LBD = Column(Integer)
    LBA = Column(Integer)
    PSH = Column(Integer)
    PSD = Column(Integer)
    PSA = Column(Integer)
    WHH = Column(Integer)
    WHD = Column(Integer)
    WHA = Column(Integer)
    SJH = Column(Integer)
    SJD = Column(Integer)
    SJA = Column(Integer)
    VCH = Column(Integer)
    VCD = Column(Integer)
    VCA = Column(Integer)
    GBH = Column(Integer)
    GBD = Column(Integer)
    GBA = Column(Integer)
    BSH = Column(Integer)
    BSD = Column(Integer)
    BSA = Column(Integer)

    def string_date(self):
        return str(self.date.day) + "/" + str(self.date.month)+ "/" + str(self.date.year)

    def __iter__(self):
        yield 'id', self.id
        yield 'country_id', self.country_id
        yield 'league_id', self.league_id
        yield 'season', self.season
        yield 'stage', self.stage
        yield 'date', self.string_date()
        yield 'match_api_id', self.match_api_id
        yield 'home_team_api_id', self.home_team_api_id
        yield 'away_team_api_id', self.away_team_api_id
        yield 'home_team_goal', self.home_team_goal
        yield 'away_team_goal', self.away_team_goal
        yield 'home_player_X1', self.home_player_X1
        yield 'home_player_X2', self.home_player_X2
        yield 'home_player_X3', self.home_player_X3
        yield 'home_player_X4', self.home_player_X4
        yield 'home_player_X5', self.home_player_X5
        yield 'home_player_X6', self.home_player_X6
        yield 'home_player_X7', self.home_player_X7
        yield 'home_player_X8', self.home_player_X8
        yield 'home_player_X9', self.home_player_X9
        yield 'home_player_X10', self.home_player_X10
        yield 'home_player_X11', self.home_player_X11
        yield 'away_player_X1', self.away_player_X1
        yield 'away_player_X2', self.away_player_X2
        yield 'away_player_X3', self.away_player_X3
        yield 'away_player_X4', self.away_player_X4
        yield 'away_player_X5', self.away_player_X5
        yield 'away_player_X6', self.away_player_X6
        yield 'away_player_X7', self.away_player_X7
        yield 'away_player_X8', self.away_player_X8
        yield 'away_player_X9', self.away_player_X9
        yield 'away_player_X10', self.away_player_X10
        yield 'away_player_X11', self.away_player_X11
        yield 'home_player_Y1', self.home_player_Y1
        yield 'home_player_Y2', self.home_player_Y2
        yield 'home_player_Y3', self.home_player_Y3
        yield 'home_player_Y4', self.home_player_Y4
        yield 'home_player_Y5', self.home_player_Y5
        yield 'home_player_Y6', self.home_player_Y6
        yield 'home_player_Y7', self.home_player_Y7
        yield 'home_player_Y8', self.home_player_Y8
        yield 'home_player_Y9', self.home_player_Y9
        yield 'home_player_Y10', self.home_player_Y10
        yield 'home_player_Y11', self.home_player_Y11
        yield 'away_player_Y1', self.away_player_Y1
        yield 'away_player_Y2', self.away_player_Y2
        yield 'away_player_Y3', self.away_player_Y3
        yield 'away_player_Y4', self.away_player_Y4
        yield 'away_player_Y5', self.away_player_Y5
        yield 'away_player_Y6', self.away_player_Y6
        yield 'away_player_Y7', self.away_player_Y7
        yield 'away_player_Y8', self.away_player_Y8
        yield 'away_player_Y9', self.away_player_Y9
        yield 'away_player_Y10', self.away_player_Y10
        yield 'away_player_Y11', self.away_player_Y11
        yield 'home_player_1', self.home_player_1
        yield 'home_player_2', self.home_player_2
        yield 'home_player_3', self.home_player_3
        yield 'home_player_4', self.home_player_4
        yield 'home_player_5', self.home_player_5
        yield 'home_player_6', self.home_player_6
        yield 'home_player_7', self.home_player_7
        yield 'home_player_8', self.home_player_8
        yield 'home_player_9', self.home_player_9
        yield 'home_player_10', self.home_player_10
        yield 'home_player_11', self.home_player_11
        yield 'away_player_1', self.away_player_1
        yield 'away_player_2', self.away_player_2
        yield 'away_player_3', self.away_player_3
        yield 'away_player_4', self.away_player_4
        yield 'away_player_5', self.away_player_5
        yield 'away_player_6', self.away_player_6
        yield 'away_player_7', self.away_player_7
        yield 'away_player_8', self.away_player_8
        yield 'away_player_9', self.away_player_9
        yield 'away_player_10', self.away_player_10
        yield 'away_player_11', self.away_player_11
        yield 'goal', self.goal
        yield 'shoton', self.shoton
        yield 'shotoff', self.shotoff
        yield 'foulcommit', self.foulcommit
        yield 'card', self.card
        yield 'cross', self.cross
        yield 'corner', self.corner
        yield 'possession', self.possession
        yield 'B365H', self.B365H
        yield 'B365D', self.B365D
        yield 'B365A', self.B365A
        yield 'BWH', self.BWH
        yield 'BWD', self.BWD
        yield 'BWA', self.BWA
        yield 'IWH', self.IWH
        yield 'IWD', self.IWD
        yield 'IWA', self.IWA
        yield 'LBH', self.LBH
        yield 'LBD', self.LBD
        yield 'LBA', self.LBA
        yield 'PSH', self.PSH
        yield 'PSD', self.PSD
        yield 'PSA', self.PSA
        yield 'WHH', self.WHH
        yield 'WHD', self.WHD
        yield 'WHA', self.WHA
        yield 'SJH', self.SJH
        yield 'SJD', self.SJD
        yield 'SJA', self.SJA
        yield 'VCH', self.VCH
        yield 'VCD', self.VCD
        yield 'VCA', self.VCA
        yield 'GBH', self.GBH
        yield 'GBD', self.GBD
        yield 'GBA', self.GBA
        yield 'BSH', self.BSH
        yield 'BSD', self.BSD
        yield 'BSA', self.BSA