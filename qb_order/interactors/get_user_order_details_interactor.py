
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
            user_orders = self.get_user_order_details(user_id)

            if not user_orders:
                return presenter.raise_order_not_found_exception()

            return presenter.get_user_order_details_response(user_orders)
        except InvalidUserIdException:
            return presenter.raise_invalid_user_id_exception()
        except Exception as e:
            return presenter.raise_unexpected_error_response(str(e))

    def get_user_order_details(self, user_id: str):

        return self.user_order_storage.get_user_order_details(user_id=user_id)
