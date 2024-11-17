from django.db import transaction

from qb_order.exceptions import NoOrdersFoundException
from qb_order.presenters.get_user_all_details_presenter import \
    GetUserOrdersPresenter
from qb_order.storages.get_user_all_details_storage import UserAllOrderStorage


class GetUserOrdersInteractor:
    def __init__(self, storage: UserAllOrderStorage,
                 presenter: GetUserOrdersPresenter):
        self.storage = storage
        self.presenter = presenter

    @transaction.atomic()
    def get_user_orders_wrapper(self, user_id: str, page_number: int,
                                page_size: int):

        try:
            if not user_id:
                return self.presenter.raise_order_not_found_exception()

            if page_number < 1 or page_size < 1:
                return self.presenter.raise_unexpected_error_response(
                    "Invalid page number or page size")

            orders_dto, total_pages = self.storage.get_paginated_user_orders(
                user_id=user_id,
                page_number=page_number,
                page_size=page_size
            )

            if not orders_dto:
                return self.presenter.raise_order_not_found_exception()

            return self.presenter.get_user_orders_response(orders_dto,
                                                           total_pages)

        except NoOrdersFoundException:
            return self.presenter.raise_order_not_found_exception()
        except ValueError as e:
            return self.presenter.raise_unexpected_error_response(
                f"ValueError: {str(e)}")
        except Exception as e:
            return self.presenter.raise_unexpected_error_response(
                f"Unexpected error: {str(e)}")
