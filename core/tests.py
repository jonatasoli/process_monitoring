from django.test import TestCase
from core.models import StatusProcess, UserProfile


class UrlValid(TestCase):
    def setUp(self):
        self.api = self.client.get('/api/')
        self.profile = self.client.get('/api/profile/')
        self.login = self.client.get('/api/login/')
        self.status = self.client.get('/api/status-process/')
        self.list = self.client.get('/consult/list/')

    def test_get(self):
        """Get /api/* must retrun status code """
        self.assertEqual(200, self.profile.status_code)
        self.assertEqual(405, self.login.status_code)
        self.assertEqual(401, self.status.status_code)
        self.assertEqual(200, self.api.status_code)
        self.assertEqual(200, self.list.status_code)


class StatusProcessModelTest(TestCase):

    def setUp(self):
        self.user = UserProfile(
                email='teste@teste.com',
                name='Test',
                url='https://test.com/postback/',
                password='123'
        )
        self.user.save()

        self.obj = StatusProcess(
                user_profile=self.user,
                id_process='12345678901',
                status_process='Em análise'
                )
        self.obj.save()

    def test_create(self):
        self.assertTrue(StatusProcess.objects.exists())
        self.assertTrue(UserProfile.objects.exists())

    def test_str(self):
        self.assertEqual('Em análise', str(self.obj))
        self.assertEqual('teste@teste.com', str(self.user))
