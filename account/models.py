from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    data_imported = models.BooleanField(default=False)

    objects = UserManager()

    class Meta(object):
        app_label = 'account'
