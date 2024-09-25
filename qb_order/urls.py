from qb_order.views import get_categories
from qb_users.urls import urlpatterns
from django.urls import path

urlpatterns=[
    path('get/categories/', get_categories.get_categories)
]