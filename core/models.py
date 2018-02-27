from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


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

    def create_superuser(self, email, name, password):
        """Create and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

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
