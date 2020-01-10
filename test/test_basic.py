from django.test import Client
from wagtail.tests.utils import WagtailPageTests
from django.contrib.auth.admin import User


class BasicWagtailTest(WagtailPageTests):
    def setUp(self) -> None:
        self.client = Client()

    def test_start(self) -> None:
        response = self.client.get('/')
        self.assertTrue(hasattr(response, 'status_code'))
        self.assertEqual(200, response.status_code)

    def test_get_admin_screen(self) -> None:
        response = self.client.get('/admin/')
        self.assertRedirects(response, "/admin/login/?next=/admin/")

    def test_login(self) -> None:
        credentials = {'username': 'cb', 'password': 'secret'}
        User.objects.create_user(**credentials, is_superuser=True, is_staff=True)
        self.assertTrue(self.client.login(**credentials))
        response = self.client.get('/admin/')
        self.assertTrue(hasattr(response, 'status_code'))
        self.assertEqual(200, response.status_code)

    def test_favicon(self) -> None:
        response = self.client.get('/favicon.ico')
        self.assertEqual(302, response.status_code)
        self.assertEqual(str(response.url)[:20], '/static/img/favicon.')

    def test_robots(self) -> None:
        response = self.client.get('/robots.txt')
        self.assertEqual(200, response.status_code)