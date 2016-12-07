from test_base import BaseTestCase
from app.models.sap import SAP
from factories.sap_factory import SapFactory


class TestDataSoccerApi(BaseTestCase):

    def setUp(self):
        SapFactory.create_batch(10)

    def tearDown(self):
        SAP.query.delete()

    def test_api_should_return_10_countries(self):
        response = self.client.get("/api/sap/")
        self.assertEqual(len(response.json['data']), 10)