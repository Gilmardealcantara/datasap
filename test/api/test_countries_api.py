from test_base import BaseTestCase
from app.models.country import Country
from factories.datasoccer_factory import CountryFactory


class TestDataSoccerApi(BaseTestCase):

    def setUp(self):
        CountryFactory.create_batch(10)

    def tearDown(self):
        Country.query.delete()

#    def test_api_should_return_10_countries(self):
#        response = self.client.get("/api/data_soccer/country")
#        self.assertEqual(len(response.json['data']), 10)