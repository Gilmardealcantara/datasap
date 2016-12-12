import pandas
import math
from flask_script import Command
from app.models.sap import SAP
from app import db

class LoadData(Command):

    "Loads SAP data"

    def run(self):
        data_frame = pandas.read_csv('data/xAPI-Edu-Data.csv')
        for (index, row) in data_frame.iterrows():
            sap = SAP()
            sap.gender = str(row['gender'])
            sap.NationalITy = str(row['NationalITy'])
            sap.PlaceofBirth = str(row['PlaceofBirth'])
            sap.StageID = str(row['StageID'])
            sap.GradeID = str(row['GradeID'])
            sap.SectionID = str(row['SectionID'])
            sap.Topic = str(row['Topic'])
            sap.Semester = str(row['Semester'])
            sap.Relation = str(row['Relation'])
            sap.raisedhands = row['raisedhands']
            sap.VisITedResources = row['VisITedResources']
            sap.AnnouncementsView = row['AnnouncementsView']
            sap.Discussion = row['Discussion']
            sap.ParentAnsweringSurvey = str(row['ParentAnsweringSurvey'])
            sap.ParentschoolSatisfaction = str(row['ParentschoolSatisfaction'])
            sap.StudentAbsenceDays = str(row['StudentAbsenceDays'])
            sap.Class = str(row['Class'])
            db.session.add(sap)
        
        db.session.commit()


