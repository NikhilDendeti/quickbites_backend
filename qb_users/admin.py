from django.contrib import admin

from qb_users.models import *
admin.site.register(UserAccount)
admin.site.register(UserProfileDetails)