from test_base import BaseTestCase


class TestDataSoccerApi(BaseTestCase):

    def test_should_respond_ok_to_data_soccer_countries_path(self):
        response = self.client.get('/api/data_soccer/countries')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_leagues_path(self):
        response = self.client.get('/api/data_soccer/leagues')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_players_path(self):
        response = self.client.get('/api/data_soccer/players')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_players_attrs_path(self):
        response = self.client.get('/api/data_soccer/players_attrs')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_sqlite_sequence_path(self):
        response = self.client.get('/api/data_soccer/sqlite_sequence')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_team_path(self):
        response = self.client.get('/api/data_soccer/team')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_team_attrs_path(self):
        response = self.client.get('/api/data_soccer/team_attrs')
        self.assert_200(response)

    def test_should_respond_ok_to_data_soccer_match_path(self):
        response = self.client.get('/api/data_soccer/match')
        self.assert_200(response)
