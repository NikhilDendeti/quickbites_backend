
from rest_framework.decorators import api_view

from qb_order.storages.get_user_order_details_storage import UserOrderStorage


@api_view(["GET"])
def get_user_order_details(request):
    user = request.user
    user_id = user.user_id
    from qb_order.interactors.get_user_order_details_interactor import \
        GetUserOrderDetailsInteractor

    from qb_order.presenters.get_user_order_details_presenter import \
        GetUserOrderDetailsPresenter

    presenter = GetUserOrderDetailsPresenter()
    user_order_storage = UserOrderStorage()
    interactor = GetUserOrderDetailsInteractor(
        user_order_storage=user_order_storage)

    return interactor.get_user_order_details_wrapper(user_id=user_id,
                                                     presenter=presenter)
