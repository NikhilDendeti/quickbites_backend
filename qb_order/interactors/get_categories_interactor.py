from qb_order.presenters.get_categories_presenter import GetCategoryPresenter
from qb_order.storages.get_categories_storages import GetCategoryStorage
from qb_order.exceptions import \
    SomeSpecificException


class GetCategoriesInteractor:
    def __init__(self, storage: GetCategoryStorage,
                 presenter: GetCategoryPresenter):
        self.storage = storage
        self.presenter = presenter

    def get_categories_wrapper(self):
        try:
            return self.get_categories()
        except SomeSpecificException:
            return self.presenter.raise_specific_exception()
        except Exception as e:
            return self.presenter.raise_unexpected_error_response(str(e))

    def get_categories(self):
        categories_dto = self.storage.get_all_categories_with_items()

        if not categories_dto:
            return self.presenter.raise_no_categories_found_exception()

        return self.presenter.get_categories_response(categories_dto)
