import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    user_id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)


class   UserProfileDetails(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    ROLE_CHOICES = [
        ('vendor', 'VENDOR'),
        ('student', 'STUDENT'),
        ('employee', 'EMPLOYEE')
    ]
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.role}"
