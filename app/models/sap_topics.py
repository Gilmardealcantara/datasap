from sqlalchemy import Column, Integer, String, Date
from app import db

class SAPTopics(db.Model):
    __tablename__ = 'sap_t'

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    raisedhands = Column(Integer)  
    visitedresources = Column(Integer)
    announcementsview = Column(Integer)
    discussion = Column(Integer)


    def __iter__(self):
        yield 'id', self.id
        yield 'topic', self.topic
        yield 'raisedhands', self.raisedhands
        yield 'visitedresources', self.visitedresources
        yield 'announcementsview', self.announcementsview
        yield 'discussion', self.discussion