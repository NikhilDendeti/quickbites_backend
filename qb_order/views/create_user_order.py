from rest_framework.decorators import api_view
from rest_framework.response import Response

from qb_order.interactors.create_user_order_interactor import \
    CreateOrUpdateOrderInteractor
from qb_order.presenters.create_user_order_presenter import \
    CreateOrUpdateOrderPresenter
from qb_order.storages.create_user_order_storage import \
    CreateOrUpdateOrderStorage


@api_view(["POST"])
def create_or_update_user_order(request):
    user = request.user
    user_id = user.user_id
    order_data = request.data

    storage = CreateOrUpdateOrderStorage()
    interactor = CreateOrUpdateOrderInteractor(storage=storage)
    presenter = CreateOrUpdateOrderPresenter()

    return interactor.create_or_update_order_wrapper(
        user_id=user_id,
        order_data=order_data,
        presenter=presenter
    )
