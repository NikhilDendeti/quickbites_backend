from django.db import transaction

from qb_order.dtos import UserOrderDTO
from qb_order.exceptions import SomeSpecificException
from qb_order.presenters.create_user_order_presenter import \
    CreateOrUpdateOrderPresenter
from qb_order.storages.create_user_order_storage import \
    CreateOrUpdateOrderStorage


class CreateOrUpdateOrderInteractor:
    def __init__(self, storage):
        self.storage = storage

    def create_or_update_order_wrapper(self, user_id: str, order_data: dict,
                                       presenter):
        try:
            # Check if the order_data contains items
            if not order_data.get('items'):
                return presenter.raise_order_not_found_exception()

            # Proceed with creating or updating the order
            order_dto = self.storage.create_or_update_order(user_id,
                                                            order_data)
            return presenter.get_order_response(order_dto)

        except SomeSpecificException:
            return presenter.raise_specific_exception()
        except Exception as e:
            return presenter.raise_unexpected_error_response(str(e))

    def create_or_update_order(self, user_id: str,
                               order_data: dict) -> UserOrderDTO:
        return self.storage.create_or_update_order(user_id, order_data)
