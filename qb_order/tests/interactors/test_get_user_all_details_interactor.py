from unittest import mock

import pytest

from qb_order.dtos import UserOrderDTO
from qb_order.exceptions import NoOrdersFoundException
from qb_order.interactors.get_user_all_orders_interactor import \
    GetUserOrdersInteractor


@pytest.mark.django_db
class TestGetUserOrdersInteractor:
    @pytest.fixture()
    def user_order_storage_mock(self):
        from qb_order.storages.get_user_all_details_storage import \
            UserAllOrderStorage
        return mock.create_autospec(UserAllOrderStorage)

    @pytest.fixture
    def presenter_mock(self):
        from qb_order.presenters.get_user_all_details_presenter import \
            GetUserOrdersPresenter
        return mock.create_autospec(GetUserOrdersPresenter)

    @pytest.fixture
    def interactor(self, user_order_storage_mock, presenter_mock):
        return GetUserOrdersInteractor(storage=user_order_storage_mock,
                                       presenter=presenter_mock)

    def test_get_user_orders_success(self, interactor, user_order_storage_mock,
                                     presenter_mock):
        # Arrange
        user_id = "27a00ec7-46f5-4e62-8fca-17ab98c004c9"
        expected_orders = [UserOrderDTO(
            order_id="order_1", total_amount=100.0,
            order_created_at="2024-01-01",
            order_updated_at="2024-01-02", user_id=user_id, status="COMPLETED",
            total_items_count=1, items=[]
        )]
        user_order_storage_mock.get_paginated_user_orders.return_value = (
        expected_orders, 1)
        presenter_mock.get_user_orders_response.return_value = "mock_response"

        # Act
        result = interactor.get_user_orders_wrapper(user_id, page_number=1,
                                                    page_size=5)

        # Assert
        user_order_storage_mock.get_paginated_user_orders.assert_called_once_with(
            user_id, 1, 5)
        presenter_mock.get_user_orders_response.assert_called_once_with(
            expected_orders, 1)
        assert result == "mock_response"

    def test_get_user_orders_no_orders_found(self, interactor,
                                             user_order_storage_mock,
                                             presenter_mock):
        # Arrange
        user_order_storage_mock.get_paginated_user_orders.side_effect = NoOrdersFoundException()
        presenter_mock.raise_order_not_found_exception.return_value = "No orders found"

        # Act
        result = interactor.get_user_orders_wrapper("nonexistent_user", 1, 5)

        # Assert
        presenter_mock.raise_order_not_found_exception.assert_called_once()
        assert result == "No orders found"
