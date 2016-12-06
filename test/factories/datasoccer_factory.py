import factory
from app import db
from app.models.country import Country


class CountryFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Country
        sqlalchemy_session = db.session
    
    
    name = 'adsasd'