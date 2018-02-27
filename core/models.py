from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models import signals
import requests


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, url, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an e-mail adress.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, url=url)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, url, password):
        """Create and saves a new superuser with given details."""

        user = self.create_user(email, name, url, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'url']

    def get_full_name(self):
        """ Used to get a users full name. """

        return self.name

    def get_short_name(self):
        """Get users short name. """

        return self.name

    def get_url(self):
        """Get users url. """

        return self.url

    def __str__(self):
        """Django uses this when needs to convert the object to a string. """

        return self.email


class StatusProcess(models.Model):
    """Process status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    id_process = models.IntegerField(unique=True)
    status_process = models.CharField(max_length=255)

    def __str__(self):
        """Return the model as a string."""
        return self.status_process


def status_post_save(signal, instance, sender, **kwargs):
    """Trigger to send post to client url"""

    user = UserProfile.objects.all().filter(pk=instance.user_profile_id)
    dict_process = {}

    dict_process['processo'] = instance.id_process
    dict_process['status'] = instance.status_process

    post_data = dict_process
    url = user.values()[0]['url']
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*"
    }

    response = requests.post(url, data=post_data, headers=headers)
    print(response)


signals.post_save.connect(status_post_save, sender=StatusProcess)
