import json


class TestGetCategoryPresenter:

    def test_get_categories_response(self, snapshot):
        from qb_order.presenters.get_categories_presenter import \
            GetCategoryPresenter
        from qb_order.dtos import CategoryDTO
        presenter = GetCategoryPresenter()

        # Arrange
        category1 = CategoryDTO(category_id=1, name="Category 1", items=[])
        category2 = CategoryDTO(category_id=2, name="Category 2", items=[])
        categories = [category1, category2]

        # Act
        response = presenter.get_categories_response(categories=categories)

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_no_categories_found_exception(self, snapshot):
        from qb_order.presenters.get_categories_presenter import \
            GetCategoryPresenter
        presenter = GetCategoryPresenter()

        # Act
        response = presenter.raise_no_categories_found_exception()

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_specific_exception(self, snapshot):
        from qb_order.presenters.get_categories_presenter import \
            GetCategoryPresenter
        presenter = GetCategoryPresenter()

        # Act
        response = presenter.raise_specific_exception()

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

    def test_raise_unexpected_error_response(self, snapshot):
        from qb_order.presenters.get_categories_presenter import \
            GetCategoryPresenter
        presenter = GetCategoryPresenter()

        # Arrange
        error_message = "Test error"

        # Act
        response = presenter.raise_unexpected_error_response(
            error_message=error_message)

        # Assert
        snapshot.assert_match(json.loads(response.content), 'response_data')

