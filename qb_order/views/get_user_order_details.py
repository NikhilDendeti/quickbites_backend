from rest_framework.decorators import api_view

from qb_order.interactors.get_user_order_details_interactor import \
    UserOrderInteractor
from qb_order.presenters.get_user_order_details_presenter import \
    UserOrderPresenter


@api_view(["POST"])
def create_user_order(request):
    user_id = request.data.get("user_id")
    total_amount = float(
        request.data.get("total_amount", 0))
    interactor = UserOrderInteractor()
    order = interactor.create_user_order(user_id, total_amount)
    return UserOrderPresenter.present_create(order)


@api_view(["GET"])
def get_user_order_details(request, user_id, order_id):
    interactor = UserOrderInteractor()
    order_details = interactor.get_user_order_details(user_id, order_id)
    return UserOrderPresenter.present_get(order_details)
