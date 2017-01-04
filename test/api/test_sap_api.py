from test_base import BaseTestCase
from app.models.sap import SAP
from factories.sap_factory import SapFactory
import logging

logging.getLogger("factory").setLevel(logging.WARN)

class TestDataSoccerApi(BaseTestCase):

    def setUp(self):
        SapFactory.create_batch(10)

    def tearDown(self):
        SAP.query.delete()

    def test_api_should_have_data(self):
        response = self.client.get("/api/sap/")
        assert "data" in response.json

    def test_api_should_return_10_countries(self):
        response = self.client.get("/api/sap/")
        self.assertEqual(len(response.json['data']), 10)

    def test_api_shold_have_fieds(self):
        response = self.client.get("/api/sap/")
        assert "AnnouncementsView" in response.json['data'][0]
        assert "Class" in response.json['data'][0]
        assert "Discussion" in response.json['data'][0]
        assert "GradeID" in response.json['data'][0]
        assert "NationalITy" in response.json['data'][0]
        assert "ParentAnsweringSurvey" in response.json['data'][0]
        assert "ParentschoolSatisfaction" in response.json['data'][0]
        assert "PlaceofBirth" in response.json['data'][0]
        assert "Relation" in response.json['data'][0]
        assert "SectionID" in response.json['data'][0]
        assert "Semester" in response.json['data'][0]
        assert "StageID" in response.json['data'][0]
        assert "StudentAbsenceDays" in response.json['data'][0]
        assert "Topic" in response.json['data'][0]
        assert "VisITedResources" in response.json['data'][0]
        assert "gender" in response.json['data'][0]
        assert "id" in response.json['data'][0]
        assert "raisedhands" in response.json['data'][0]
