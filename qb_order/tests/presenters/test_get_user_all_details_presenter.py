import json

from qb_order.dtos import UserOrderDTO, OrderItemDTO
from qb_order.presenters.get_user_all_details_presenter import \
    GetUserOrdersPresenter


class TestGetUserOrdersPresenter:

    def test_get_user_orders_response(self, snapshot):
        presenter = GetUserOrdersPresenter()

        # Arrange
        order = UserOrderDTO(
            order_id="order_1", total_amount=200.0,
            order_created_at="2024-01-01",
            order_updated_at="2024-01-02", user_id="user_1",
            status="COMPLETED",
            total_items_count=1, items=[
                OrderItemDTO(item_id="item_1", count=2, total_amount=100.0)
            ]
        )
        orders = [order]

        # Act
        response = presenter.get_user_orders_response(orders, total_pages=1)

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_order_not_found_exception(self, snapshot):
        presenter = GetUserOrdersPresenter()

        # Act
        response = presenter.raise_order_not_found_exception()

        # Assert
        assert response.status_code == 404
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_unexpected_error_response(self, snapshot):
        presenter = GetUserOrdersPresenter()

        # Arrange
        error_message = "Test error"

        # Act
        response = presenter.raise_unexpected_error_response(error_message)

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')
