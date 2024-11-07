import json
from unittest import mock

from qb_order.dtos import UserOrderDTO


class TestGetUserOrderDetailsPresenter:

    def test_get_user_order_details_response(self, snapshot):
        from qb_order.presenters.get_user_order_details_presenter import GetUserOrderDetailsPresenter
        presenter = GetUserOrderDetailsPresenter()

        # Arrange
        mock_order_details = mock.Mock(spec=UserOrderDTO)
        mock_order_details.to_dict.return_value = {
            "order_id": "1", "status": "IN_PROGRESS", "total_amount": 200.0
        }

        # Act
        response = presenter.get_user_order_details_response(mock_order_details)

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_order_not_found_exception(self, snapshot):
        from qb_order.presenters.get_user_order_details_presenter import GetUserOrderDetailsPresenter
        presenter = GetUserOrderDetailsPresenter()

        # Act
        response = presenter.raise_order_not_found_exception()

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_invalid_user_id_exception(self, snapshot):
        from qb_order.presenters.get_user_order_details_presenter import GetUserOrderDetailsPresenter
        presenter = GetUserOrderDetailsPresenter()

        # Act
        response = presenter.raise_invalid_user_id_exception()

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_unexpected_error_response(self, snapshot):
        from qb_order.presenters.get_user_order_details_presenter import GetUserOrderDetailsPresenter
        presenter = GetUserOrderDetailsPresenter()

        # Arrange
        error_message = "Test error"

        # Act
        response = presenter.raise_unexpected_error_response(error_message=error_message)

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')
