from qb_order.exceptions import InvalidUserIdException
from qb_order.presenters.get_user_order_details_presenter import \
    GetUserOrderDetailsPresenter
from qb_order.storages.get_user_order_details_storage import UserOrderStorage


class GetUserOrderDetailsInteractor:
    def __init__(self, user_order_storage: UserOrderStorage):
        self.user_order_storage = user_order_storage

    def get_user_order_details_wrapper(
            self, user_id: str, presenter: GetUserOrderDetailsPresenter):
        try:
            return self.get_user_order_details(user_id, presenter)
        except InvalidUserIdException:
            return presenter.raise_invalid_user_id_exception()
        except Exception as e:
            return presenter.raise_unexpected_error_response(str(e))

    def get_user_order_details(self, user_id: str,
                               presenter: GetUserOrderDetailsPresenter):
        user_orders = self.user_order_storage.get_user_order_details(
            user_id=user_id)

        if user_orders is None:
            return presenter.raise_order_not_found_exception()

        return presenter.get_user_order_details_response(user_orders)
