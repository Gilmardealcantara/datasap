import factory
from app import db
from app.models.sap import SAP


class SapFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = SAP
        sqlalchemy_session = db.session


    gender = 'ASDASDASDA'
    NationalITy = 'ASDASDASDA'
    PlaceofBirth = 'ASDASDASDA'
    StageID = 'ASDASDASDA'
    GradeID = 'ASDASDASDA'
    SectionID = 'ASDASDASDA'
    Topic = 'ASDASDASDA'
    Semester = 'ASDASDASDA'
    Relation = 'ASDASDASDA'
    raisedhands = 11
    VisITedResources = 124
    AnnouncementsView = 124
    Discussion = 124
    ParentAnsweringSurvey = 'DSADASDASDAS'
    ParentschoolSatisfaction = 'DSADASDASDAS'
    StudentAbsenceDays = 'DSADASDASDAS'
    Class = 'DSADASDASDAS'
