from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
         User.objects.create(username='user12', email='user@user.ru')

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email address')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 150)
