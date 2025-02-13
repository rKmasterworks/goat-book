from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertIn("<title>To-Do lists</title>", )
        self.assertTrue(response("<html>"))
        self.assertTrue(response("</html>"))