from django.test import TestCase, Client
from sssoon.forms import NewsletterForm


class NewsletterFormTests(TestCase):

    def test_valid_data(self):
        """Fill the form with test data and validate."""
        form = NewsletterForm({
            'email': "tguy@example.com"
        })
        self.assertTrue(form.is_valid())

    def test_post_form(self):
        c = Client()
        response = c.post('/signup/', {
            'email': "tguy@example.com"
        })
        self.assertEqual(response.status_code, 200)
