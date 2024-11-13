# import pytest
# from unittest import mock
#
# from qb_order.exceptions import SomeSpecificException
# from qb_order.tests.factories.models import CategoryFactory
#
#
# @pytest.mark.django_db
# class TestCategoryInteractor:
#     @pytest.fixture()
#     def category_storage_mock(self):
#         from qb_order.storages.get_categories_storages import \
#             GetCategoryStorage
#         return mock.create_autospec(GetCategoryStorage)
#
#     @pytest.fixture
#     def interactor(self, category_storage_mock, presenter_mock):
#         from qb_order.interactors.get_categories_interactor import \
#             GetCategoriesInteractor
#         return GetCategoriesInteractor(storage=category_storage_mock,
#                                        presenter=presenter_mock)
#
#     @pytest.fixture
#     def presenter_mock(self):
#         from qb_order.presenters.get_categories_presenter import \
#             GetCategoryPresenter
#         return mock.create_autospec(GetCategoryPresenter)
#
#     def test_get_categories_wrapper_success(self, interactor,
#                                             category_storage_mock):
#         # Arrange
#         category1 = CategoryFactory(name='Category 1')
#         category2 = CategoryFactory(name='Category 2')
#
#         expected_categories_dto = [
#             {"name": category1.name, "id": category1.category_id},
#             {"name": category2.name, "id": category2.category_id},
#         ]
#
#         category_storage_mock.get_all_categories_with_items.return_value = expected_categories_dto
#         mock_response = "mock_response"
#         interactor.presenter.get_categories_response.return_value = mock_response
#
#         # Act
#         result = interactor.get_categories_wrapper()
#
#         # Assert
#         category_storage_mock.get_all_categories_with_items.assert_called_once()
#         interactor.presenter.get_categories_response.assert_called_once_with(
#             expected_categories_dto)
#         assert result == mock_response
#
#     def test_get_categories_success(self, interactor, category_storage_mock):
#         # Arrange
#         category1 = CategoryFactory(name='Category 1')
#         category2 = CategoryFactory(name='Category 2')
#
#         expected_categories_dto = [
#             {"name": category1.name, "id": category1.category_id},
#             {"name": category2.name, "id": category2.category_id},
#         ]
#
#         category_storage_mock.get_all_categories_with_items.return_value = expected_categories_dto
#         mock_response = "mock_response"
#         interactor.presenter.get_categories_response.return_value = mock_response
#
#         # Act
#         result = interactor.get_categories_wrapper()
#
#         # Assert
#         category_storage_mock.get_all_categories_with_items.assert_called_once()
#         interactor.presenter.get_categories_response.assert_called_once_with(
#             expected_categories_dto)
#         assert result == mock_response
#
#     def test_get_categories_no_categories_found(self, interactor,
#                                                 category_storage_mock):
#         # Arrange
#         category_storage_mock.get_all_categories_with_items.return_value = None
#         interactor.presenter.raise_no_categories_found_exception.return_value = "No categories found"
#
#         # Act
#         result = interactor.get_categories_wrapper()
#
#         # Assert
#         category_storage_mock.get_all_categories_with_items.assert_called_once()
#         interactor.presenter.raise_no_categories_found_exception.assert_called_once()
#         assert result == "No categories found"
#
#     def test_get_categories_specific_exception(self, interactor):
#         # Arrange
#         interactor.get_categories = mock.Mock(
#             side_effect=SomeSpecificException
#             # Ensure this matches the expected custom exception
#         )
#         interactor.presenter.raise_specific_exception.return_value = "Specific exception raised"
#
#         # Act
#         result = interactor.get_categories_wrapper()
#
#         # Assert
#         interactor.presenter.raise_specific_exception.assert_called_once()
#         assert result == "Specific exception raised"
#
#     def test_get_categories_unexpected_exception(self, interactor):
#         # Arrange
#         exception_message = "Unexpected error occurred"
#         interactor.get_categories = mock.Mock(
#             side_effect=Exception(exception_message))
#         interactor.presenter.raise_unexpected_error_response.return_value = "Unexpected error response"
#
#         # Act
#         result = interactor.get_categories_wrapper()
#
#         # Assert
#         interactor.presenter.raise_unexpected_error_response.assert_called_once_with(
#             exception_message)
#         assert result == "Unexpected error response"



import pytest
from unittest import mock

from qb_order.exceptions import SomeSpecificException
from qb_order.tests.factories.models import CategoryFactory


@pytest.mark.django_db
class TestCategoryInteractor:
    @pytest.fixture()
    def category_storage_mock(self):
        from qb_order.storages.get_categories_storages import GetCategoryStorage
        return mock.create_autospec(GetCategoryStorage)

    @pytest.fixture
    def interactor(self, category_storage_mock):
        from qb_order.interactors.get_categories_interactor import GetCategoriesInteractor
        return GetCategoriesInteractor(storage=category_storage_mock)

    @pytest.fixture
    def presenter_mock(self):
        from qb_order.presenters.get_categories_presenter import GetCategoryPresenter
        return mock.create_autospec(GetCategoryPresenter)

    def test_get_categories_wrapper_success(self, interactor, category_storage_mock, presenter_mock):
        # Arrange
        category1 = CategoryFactory(name='Category 1')
        category2 = CategoryFactory(name='Category 2')

        expected_categories_dto = [
            {"name": category1.name, "id": category1.category_id},
            {"name": category2.name, "id": category2.category_id},
        ]

        category_storage_mock.get_all_categories_with_items.return_value = expected_categories_dto
        presenter_mock.get_categories_response.return_value = "mock_response"

        # Act
        result = interactor.get_categories_wrapper(presenter=presenter_mock)

        # Assert
        category_storage_mock.get_all_categories_with_items.assert_called_once()
        presenter_mock.get_categories_response.assert_called_once_with(expected_categories_dto)
        assert result == "mock_response"

    def test_get_categories_no_categories_found(self, interactor, category_storage_mock, presenter_mock):
        # Arrange
        category_storage_mock.get_all_categories_with_items.return_value = None
        presenter_mock.raise_no_categories_found_exception.return_value = "No categories found"

        # Act
        result = interactor.get_categories_wrapper(presenter=presenter_mock)

        # Assert
        category_storage_mock.get_all_categories_with_items.assert_called_once()
        presenter_mock.raise_no_categories_found_exception.assert_called_once()
        assert result == "No categories found"

    def test_get_categories_specific_exception(self, interactor, presenter_mock):
        # Arrange
        interactor.get_categories = mock.Mock(side_effect=SomeSpecificException)
        presenter_mock.raise_specific_exception.return_value = "Specific exception raised"

        # Act
        result = interactor.get_categories_wrapper(presenter=presenter_mock)

        # Assert
        presenter_mock.raise_specific_exception.assert_called_once()
        assert result == "Specific exception raised"

    def test_get_categories_unexpected_exception(self, interactor, presenter_mock):
        # Arrange
        exception_message = "Unexpected error occurred"
        interactor.get_categories = mock.Mock(side_effect=Exception(exception_message))
        presenter_mock.raise_unexpected_error_response.return_value = "Unexpected error response"

        # Act
        result = interactor.get_categories_wrapper(presenter=presenter_mock)

        # Assert
        presenter_mock.raise_unexpected_error_response.assert_called_once_with(exception_message)
        assert result == "Unexpected error response"
