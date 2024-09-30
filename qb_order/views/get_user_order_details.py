from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.exceptions import ValidationError

from qb_order.interactors.get_user_order_details_interactor import \
    CreateUserOrderInteractor
from qb_order.presenters.get_user_order_details_presenter import \
    CreateUserOrderPresenter
from qb_order.storages.get_user_order_details_storage import UserOrderStorage


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def create_user_order(request):
    request_data = request.data

    storage = UserOrderStorage()
    interactor = CreateUserOrderInteractor(storage)
    presenter = CreateUserOrderPresenter()

    try:
        order_data = interactor.execute(request_body=request_data)
        response = presenter.present_order_creation_success(order_data)

    except ValidationError as e:
        response = presenter.present_invalid_order_data(e.detail)

    except Exception as e:
        response = presenter.present_order_creation_failure(str(e))

    return response
