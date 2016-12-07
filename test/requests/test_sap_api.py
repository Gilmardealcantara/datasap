from test_base import BaseTestCase


class TestDataSoccerApi(BaseTestCase):

    def test_should_respond_ok_to_data_soccer_countries_path(self):
        response = self.client.get('/api/sap/')
        self.assert_200(response)