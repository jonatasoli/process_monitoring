from django.test import TestCase
from core.models import StatusProcess


class UrlValid(TestCase):
    def setUp(self):
        self.api = self.client.get('/api/')
        self.profile = self.client.get('/api/profile/')
        self.login = self.client.get('/api/login/')
        self.status = self.client.get('/api/status-process/')

    def test_get(self):
        """Get /api/* must retrun status code """
        self.assertEqual(200, self.profile.status_code)
        self.assertEqual(405, self.login.status_code)
        self.assertEqual(200, self.status.status_code)
        self.assertEqual(200, self.api.status_code)


class StatusProcessModelTest(TestCase):

    def setUp(self):
        self.obj = StatusProcess(
                userprofile='1',
                id_process='12345678901',
                status_process='Em análise'
                )
        self.obj.save()

    def test_create(self):
        self.assertTrue(StatusProcess.objects.exists())

    def test_str(self):
        self.assertEqual('Em análise', str(self.obj))
