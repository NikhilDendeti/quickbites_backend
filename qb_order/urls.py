from qb_order.views import get_categories
from django.urls import path

from django.urls import path

from qb_order.views.get_categories import get_categories
from qb_order.views.get_user_order_details import create_user_order

urlpatterns = [
    path('get/categories/', get_categories),
    path('create/user/order/',create_user_order)

]
