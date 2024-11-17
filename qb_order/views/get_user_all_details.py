from rest_framework.decorators import api_view
from rest_framework.response import Response
from qb_order.interactors.get_user_all_orders_interactor import GetUserOrdersInteractor
from qb_order.presenters.get_user_all_details_presenter import GetUserOrdersPresenter
from qb_order.storages.get_user_all_details_storage import UserAllOrderStorage


@api_view(["POST"])
def get_user_orders(request):
    user_id = request.data.get('user_id')
    if not user_id:
        return Response({"message": "User ID is required"}, status=400)

    try:
        page_number = int(request.data.get('page', 1))
        page_size = int(request.data.get('page_size', 5))
    except ValueError:
        return Response({"message": "Invalid page number or page size"}, status=400)

    storage = UserAllOrderStorage()
    presenter = GetUserOrdersPresenter()
    interactor = GetUserOrdersInteractor(storage=storage, presenter=presenter)

    return interactor.get_user_orders_wrapper(user_id=user_id, page_number=page_number, page_size=page_size)
