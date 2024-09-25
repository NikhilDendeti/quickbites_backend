import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes

from qb_order.interactors.get_categories_interactor import \
    GetCategoriesInteractor
from qb_order.models.items import FoodItem, Category
from qb_order.presenters.get_categories_presenter import GetCategoryPresenter
from qb_order.storages.get_categories_storages import GetCategoryStorage


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    storage = GetCategoryStorage()
    presenter = GetCategoryPresenter()
    interactor = GetCategoriesInteractor(storage=storage, presenter=presenter)
    response_data = interactor.get_categories()
    return Response(response_data)
