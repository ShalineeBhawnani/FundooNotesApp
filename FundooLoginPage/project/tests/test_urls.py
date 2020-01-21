from django.test import SimpleTestCase
from django.urls import reverse, resolve
from snippets.views import Login, Registrations


class TestUrls(SimpleTestCase):
    def test_login(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Login)