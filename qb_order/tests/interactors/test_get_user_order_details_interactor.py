# import pytest
# from unittest import mock
# from qb_order.exceptions import InvalidUserIdException
#
#
# @pytest.mark.django_db
# class TestGetUserOrderDetailsInteractor:
#     @pytest.fixture()
#     def user_order_storage_mock(self):
#         from qb_order.storages.get_user_order_details_storage import UserOrderStorage
#         return mock.create_autospec(UserOrderStorage)
#
#     @pytest.fixture
#     def presenter_mock(self):
#         from qb_order.presenters.get_user_order_details_presenter import GetUserOrderDetailsPresenter
#         return mock.create_autospec(GetUserOrderDetailsPresenter)
#
#     @pytest.fixture
#     def interactor(self, user_order_storage_mock, presenter_mock):
#         from qb_order.interactors.get_user_order_details_interactor import GetUserOrderDetailsInteractor
#         return GetUserOrderDetailsInteractor(user_order_storage=user_order_storage_mock)
#
#     def test_get_user_order_details_success(self, interactor, user_order_storage_mock, presenter_mock):
#         # Arrange
#         mock_user_order_dto = mock.Mock()
#         user_order_storage_mock.get_user_order_details.return_value = mock_user_order_dto
#         presenter_mock.get_user_order_details_response.return_value = "success_response"
#
#         # Act
#         result = interactor.get_user_order_details("1", presenter_mock)
#
#         # Assert
#         user_order_storage_mock.get_user_order_details.assert_called_once_with(user_id="1")
#         presenter_mock.get_user_order_details_response.assert_called_once_with(mock_user_order_dto)
#         assert result == "success_response"
#
#     def test_get_user_order_details_not_found(self, interactor, user_order_storage_mock, presenter_mock):
#         # Arrange
#         user_order_storage_mock.get_user_order_details.return_value = None
#         presenter_mock.raise_order_not_found_exception.return_value = "order_not_found"
#
#         # Act
#         result = interactor.get_user_order_details("1", presenter_mock)
#
#         # Assert
#         user_order_storage_mock.get_user_order_details.assert_called_once_with(user_id="1")
#         presenter_mock.raise_order_not_found_exception.assert_called_once()
#         assert result == "order_not_found"
#
#     def test_get_user_order_details_invalid_user(self, interactor, user_order_storage_mock, presenter_mock):
#         # Arrange
#         user_order_storage_mock.get_user_order_details.side_effect = InvalidUserIdException()
#         presenter_mock.raise_invalid_user_id_exception.return_value = "invalid_user"
#
#         # Act
#         result = interactor.get_user_order_details_wrapper("invalid_user_id", presenter_mock)
#
#         # Assert
#         presenter_mock.raise_invalid_user_id_exception.assert_called_once()
#         assert result == "invalid_user"
#
#     def test_get_user_order_details_unexpected_exception(self, interactor, user_order_storage_mock, presenter_mock):
#         # Arrange
#         user_order_storage_mock.get_user_order_details.side_effect = Exception("Unexpected error")
#         presenter_mock.raise_unexpected_error_response.return_value = "unexpected_error"
#
#         # Act
#         result = interactor.get_user_order_details_wrapper("1", presenter_mock)
#
#         # Assert
#         presenter_mock.raise_unexpected_error_response.assert_called_once_with("Unexpected error")
#         assert result == "unexpected_error"


import pytest
from unittest import mock
from qb_order.exceptions import InvalidUserIdException


@pytest.mark.django_db
class TestGetUserOrderDetailsInteractor:
    @pytest.fixture()
    def user_order_storage_mock(self):
        from qb_order.storages.get_user_order_details_storage import UserOrderStorage
        return mock.create_autospec(UserOrderStorage)

    @pytest.fixture
    def presenter_mock(self):
        from qb_order.presenters.get_user_order_details_presenter import GetUserOrderDetailsPresenter
        return mock.create_autospec(GetUserOrderDetailsPresenter)

    @pytest.fixture
    def interactor(self, user_order_storage_mock):
        from qb_order.interactors.get_user_order_details_interactor import GetUserOrderDetailsInteractor
        return GetUserOrderDetailsInteractor(user_order_storage=user_order_storage_mock)

    def test_get_user_order_details_success(self, interactor, user_order_storage_mock, presenter_mock):
        # Arrange
        mock_user_order_dto = mock.Mock()
        user_order_storage_mock.get_user_order_details.return_value = mock_user_order_dto
        presenter_mock.get_user_order_details_response.return_value = "success_response"

        # Act
        result = interactor.get_user_order_details_wrapper(user_id="1", presenter=presenter_mock)

        # Assert
        user_order_storage_mock.get_user_order_details.assert_called_once_with(user_id="1")
        presenter_mock.get_user_order_details_response.assert_called_once_with(mock_user_order_dto)
        assert result == "success_response"

    def test_get_user_order_details_not_found(self, interactor, user_order_storage_mock, presenter_mock):
        # Arrange
        user_order_storage_mock.get_user_order_details.return_value = None
        presenter_mock.raise_order_not_found_exception.return_value = "order_not_found"

        # Act
        result = interactor.get_user_order_details_wrapper(user_id="1", presenter=presenter_mock)

        # Assert
        user_order_storage_mock.get_user_order_details.assert_called_once_with(user_id="1")
        presenter_mock.raise_order_not_found_exception.assert_called_once()
        assert result == "order_not_found"

    def test_get_user_order_details_invalid_user(self, interactor, user_order_storage_mock, presenter_mock):
        # Arrange
        user_order_storage_mock.get_user_order_details.side_effect = InvalidUserIdException()
        presenter_mock.raise_invalid_user_id_exception.return_value = "invalid_user"

        # Act
        result = interactor.get_user_order_details_wrapper(user_id="invalid_user_id", presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_user_id_exception.assert_called_once()
        assert result == "invalid_user"

    def test_get_user_order_details_unexpected_exception(self, interactor, user_order_storage_mock, presenter_mock):
        # Arrange
        user_order_storage_mock.get_user_order_details.side_effect = Exception("Unexpected error")
        presenter_mock.raise_unexpected_error_response.return_value = "unexpected_error"

        # Act
        result = interactor.get_user_order_details_wrapper(user_id="1", presenter=presenter_mock)

        # Assert
        presenter_mock.raise_unexpected_error_response.assert_called_once_with("Unexpected error")
        assert result == "unexpected_error"
