from sqlalchemy import Column, Integer, String, Date
from app import db


class SAP(db.Model):
    __tablename__ = 'sap'

    id = Column(Integer, primary_key=True)
    gender = Column(String)     # M   
    NationalITy = Column(String)        # KW
    PlaceofBirth = Column(String)       # KuwaIT
    StageID = Column(String)        # lowerlevel
    GradeID = Column(String)        # G-02
    SectionID = Column(String)      # B
    Topic = Column(String)      # IT
    Semester = Column(String)       # F
    Relation = Column(String)       # Father
    raisedhands = Column(Integer)        # 50
    VisITedResources = Column(Integer)       # 7
    AnnouncementsView = Column(Integer)      # 9
    Discussion = Column(Integer)     # 50
    ParentAnsweringSurvey = Column(String)      # Yes
    ParentschoolSatisfaction = Column(String)       # Bad
    StudentAbsenceDays = Column(String)     # Above-7
    Class = Column(String)      # M

    def __iter__(self):
        yield 'id', self.id
        yield 'gender', self.gender
        yield 'NationalITy', self.NationalITy
        yield 'PlaceofBirth', self.PlaceofBirth
        yield 'StageID', self.StageID
        yield 'GradeID', self.GradeID
        yield 'SectionID', self.SectionID
        yield 'Topic', self.Topic
        yield 'Semester', self.Semester
        yield 'Relation', self.Relation
        yield 'raisedhands', self.raisedhands
        yield 'VisITedResources', self.VisITedResources
        yield 'AnnouncementsView', self.AnnouncementsView
        yield 'Discussion', self.Discussion
        yield 'ParentAnsweringSurvey', self.ParentAnsweringSurvey
        yield 'ParentschoolSatisfaction', self.ParentschoolSatisfaction
        yield 'StudentAbsenceDays', self.StudentAbsenceDays
        yield 'Class', self.Class
