from qb_order.views import get_categories
from django.urls import path

from django.urls import path

from qb_order.views.get_categories import get_categories
from qb_order.views.get_user_order_details import get_user_order_details

urlpatterns = [
    path('get/categories/', get_categories),
    path('get/user/orders/details/', get_user_order_details)

]
