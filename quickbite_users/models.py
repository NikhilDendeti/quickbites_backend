from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE


class UserAccount(AbstractUser):
    pass


class UserRoleProfile(models.Model):
    ROLE_CHOICES = [
        ('vendor', 'VENDOR'),
        ('student', 'STUDENT'),
        ('employee', 'EMPLOYEE')
    ]
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.role}"


# request_body = {
#     "username": "str"
# }
#
# response_200 = {
#     "role_type": "str",
#     "enum":[
#         ""
#     ]
# }
#
# response_400 = {
#     " invalid username",
#
# }
