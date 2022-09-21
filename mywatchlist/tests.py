from django.test import TestCase

# Create your tests here.
class BasicTest(TestCase):
    def test_html(self):
        response = self.client.get('mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    