# from rest_framework.decorators import api_view
#
# from qb_order.interactors.get_categories_interactor import \
#     GetCategoriesInteractor
# from qb_order.presenters.get_categories_presenter import GetCategoryPresenter
# from qb_order.storages.get_categories_storages import GetCategoryStorage
#
#
# @api_view(["GET"])
# def get_categories(request):
#     storage = GetCategoryStorage()
#     presenter = GetCategoryPresenter()
#     interactor = GetCategoriesInteractor(storage=storage, presenter=presenter)
#
#     return interactor.get_categories_wrapper()


from rest_framework.decorators import api_view

from qb_order.interactors.get_categories_interactor import GetCategoriesInteractor
from qb_order.presenters.get_categories_presenter import GetCategoryPresenter
from qb_order.storages.get_categories_storages import GetCategoryStorage


@api_view(["GET"])
def get_categories(request):
    """
    Django view to fetch categories.
    """
    storage = GetCategoryStorage()
    interactor = GetCategoriesInteractor(storage=storage)
    presenter = GetCategoryPresenter()

    return interactor.get_categories_wrapper(presenter=presenter)
