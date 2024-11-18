import json

from qb_order.dtos import UserOrderDTO, OrderItemDTO
from qb_order.presenters.create_user_order_presenter import \
    CreateOrUpdateOrderPresenter


class TestCreateOrUpdateOrderPresenter:

    def test_get_order_response(self, snapshot):
        presenter = CreateOrUpdateOrderPresenter()

        items = [OrderItemDTO(item_id="item1", count=1, total_amount=100.0)]
        order = UserOrderDTO(
            order_id="order123",
            total_amount=100.0,
            order_created_at="2024-11-18T06:42:30",
            order_updated_at="2024-11-18T06:45:55",
            user_id="user123",
            status="IN_PROGRESS",
            total_items_count=1,
            items=items
        )

        response = presenter.get_order_response(order)
        snapshot.assert_match(json.loads(response.content), "response_data")

    def test_raise_order_not_found_exception(self):
        presenter = CreateOrUpdateOrderPresenter()

        response = presenter.raise_order_not_found_exception()
        assert json.loads(response.content) == {"message": "Order not found"}

    def test_raise_specific_exception(self):
        presenter = CreateOrUpdateOrderPresenter()

        response = presenter.raise_specific_exception()
        assert json.loads(response.content) == {
            "message": "A specific error occurred"}

    def test_raise_unexpected_error_response(self):
        presenter = CreateOrUpdateOrderPresenter()

        response = presenter.raise_unexpected_error_response(
            "Unexpected error")
        assert json.loads(response.content) == {
            "message": "Unexpected error: Unexpected error"}
