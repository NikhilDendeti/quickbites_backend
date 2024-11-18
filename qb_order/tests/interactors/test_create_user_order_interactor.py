from unittest import mock

import pytest

from qb_order.dtos import UserOrderDTO, OrderItemDTO
from qb_order.exceptions import SomeSpecificException
from qb_order.interactors.create_user_order_interactor import \
    CreateOrUpdateOrderInteractor
from qb_order.presenters.create_user_order_presenter import \
    CreateOrUpdateOrderPresenter
from qb_order.storages.create_user_order_storage import \
    CreateOrUpdateOrderStorage


@pytest.mark.django_db
class TestCreateOrUpdateOrderInteractor:

    @pytest.fixture()
    def storage_mock(self):
        return mock.create_autospec(CreateOrUpdateOrderStorage)

    @pytest.fixture()
    def presenter_mock(self):
        return mock.create_autospec(CreateOrUpdateOrderPresenter)

    @pytest.fixture()
    def interactor(self, storage_mock):
        return CreateOrUpdateOrderInteractor(storage=storage_mock)

    def test_create_order_success(self, interactor, storage_mock,
                                  presenter_mock):
        # Arrange
        user_id = "user123"
        order_data = {
            "items": [{"item_id": "item1"}, {"item_id": "item2"}]
        }
        items_dto = [
            OrderItemDTO(item_id="item1", count=1, total_amount=100.0),
            OrderItemDTO(item_id="item2", count=1, total_amount=50.0)
        ]
        order_dto = UserOrderDTO(
            order_id="order1",
            total_amount=150.0,
            order_created_at="2024-11-18T06:42:30.123456",
            order_updated_at="2024-11-18T06:45:55.654321",
            user_id=user_id,
            status="IN_PROGRESS",
            total_items_count=2,
            items=items_dto
        )

        storage_mock.create_or_update_order.return_value = order_dto
        presenter_mock.get_order_response.return_value = "mock_response"

        # Act
        result = interactor.create_or_update_order_wrapper(
            user_id=user_id,
            order_data=order_data,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_or_update_order.assert_called_once_with(user_id,
                                                                    order_data)
        presenter_mock.get_order_response.assert_called_once_with(order_dto)
        assert result == "mock_response"

    def test_no_items_in_order(self, interactor, storage_mock, presenter_mock):
        # Arrange
        user_id = "user123"
        order_data = {"items": []}
        presenter_mock.raise_order_not_found_exception.return_value = "No items found"

        # Act
        result = interactor.create_or_update_order_wrapper(
            user_id=user_id,
            order_data=order_data,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_order_not_found_exception.assert_called_once()
        assert result == "No items found"

    def test_specific_exception(self, interactor, presenter_mock):
        # Arrange
        user_id = "user123"
        order_data = {"items": [{"item_id": "item1"}]}
        interactor.storage.create_or_update_order = mock.Mock(
            side_effect=SomeSpecificException)
        presenter_mock.raise_specific_exception.return_value = "Specific exception raised"

        # Act
        result = interactor.create_or_update_order_wrapper(
            user_id=user_id,
            order_data=order_data,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_specific_exception.assert_called_once()
        assert result == "Specific exception raised"

    def test_unexpected_exception(self, interactor, presenter_mock):
        # Arrange
        user_id = "user123"
        order_data = {"items": [{"item_id": "item1"}]}
        interactor.storage.create_or_update_order = mock.Mock(
            side_effect=Exception("Unexpected error"))
        presenter_mock.raise_unexpected_error_response.return_value = "Unexpected error response"

        # Act
        result = interactor.create_or_update_order_wrapper(
            user_id=user_id,
            order_data=order_data,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_unexpected_error_response.assert_called_once_with(
            "Unexpected error")
        assert result == "Unexpected error response"
