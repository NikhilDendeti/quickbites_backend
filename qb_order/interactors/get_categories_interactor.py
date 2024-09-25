class GetCategoriesInteractor:
    def __init__(self, storage, presenter):
        self.storage = storage
        self.presenter = presenter

    def get_categories(self):
        categories_dto = self.storage.get_all_categories_with_items()
        response_data = self.presenter.get_categories_response(categories_dto)
        return response_data
