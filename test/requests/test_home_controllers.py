from test_base import BaseTestCase


class TestHomeController(BaseTestCase):

    def test_home_path_should_be_ok(self):
        response = self.client.get("/")
        self.assert_200(response)

    def test_tables_path_should_be_ok(self):
        response = self.client.get("/tables")
        self.assert_200(response)

    def test_views_path_should_be_ok(self):
        response = self.client.get("/views")
        self.assert_200(response)
