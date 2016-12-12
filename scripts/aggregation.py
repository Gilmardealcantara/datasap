from flask_script import Command
from sqlalchemy import create_engine
from app import flask
from app.models.sap import SAP

class AggregationData(Command):
    "Aggregation SAP data by topics"

    def run(self):

        engine = create_engine(flask.config['SQLALCHEMY_DATABASE_URI'])
        connection = engine.connect()

        sql = "DROP TABLE sap_t; CREATE TABLE sap_t(\
                id SERIAL PRIMARY KEY,\
                Topic   VARCHAR(20),\
                raisedhands INTEGER,\
                VisITedResources INTEGER,\
                AnnouncementsView INTEGER,\
                Discussion INTEGER\
            )"
        connection.execute(sql);

        saps = SAP.query.all()
        data={}

        for row in [dict(c) for c in saps]:
            if data.has_key(row['Topic']) : 
                data[row['Topic']] = [data[row['Topic']][0] + 1, data[row['Topic']][1] + row['raisedhands'],  data[row['Topic']][2] + row['VisITedResources'],  data[row['Topic']][3] + row['AnnouncementsView'],  data[row['Topic']][4] + row['Discussion']]
            else:
                data[row['Topic']] = [1, row['raisedhands'], row['VisITedResources'], row['AnnouncementsView'], row['Discussion']]

        for topic in data:
            sql = "INSERT INTO sap_t(Topic, raisedhands, VisITedResources, AnnouncementsView, Discussion)\
                    VALUES ('"+ str(topic) + "', " + str(data[topic][1] / data[topic][0]) + ", " + str(data[topic][2] / data[topic][0]) + ", " + str(data[topic][3] / data[topic][0]) + ", " + str(data[topic][4] / data[topic][0]) + ")"
            connection.execute(sql);
        

        print 'Aggregation OK !'        