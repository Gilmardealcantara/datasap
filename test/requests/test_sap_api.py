from test_base import BaseTestCase


class TestDataSoccerApi(BaseTestCase):

    def test_should_respond_ok_to_datasap(self):
        response = self.client.get('/api/sap/')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_data_tables(self):
        response = self.client.get('/api/sap/data_tables')
        self.assert_200(response)

    def test_should_respond_ok_to_data_graph_one(self):
        response = self.client.get('/api/sap/graph/1')
        self.assert_200(response)

    def test_should_respond_ok_to_data_grap_two(self):
        response = self.client.get('/api/sap/graph/2')
        self.assert_200(response)

