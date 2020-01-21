from django.test import SimpleTestCase
from django.urls import reverse, resolve
from snippets.views import Login, Registrations, ForgotPassword

class TestUrls(SimpleTestCase):
    def test_login(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Login)

    def test_registration(self):
        url = reverse('registration')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Registrations)

    def test_forgot_Password(self):
        url = reverse('forgot_Password')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ForgotPassword)

