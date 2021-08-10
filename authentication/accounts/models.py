from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_activated = models.BooleanField(default=False, db_index=True, verbose_name='Is user active?')
    send_messages = models.BooleanField(default=False, db_index=True, verbose_name='Send notifications?')

    # class Meta(AbstractUser.Meta):
    #     pass