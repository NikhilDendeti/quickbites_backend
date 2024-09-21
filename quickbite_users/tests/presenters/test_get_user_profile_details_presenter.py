import json
from snapshottest import TestCase

from quickbite_users.tests.factories.dtos import \
    UserProfileCompleteDetailsDTOFactory


class TestGetUserDetailsPresenter(TestCase):
    def test_for_invalid_user_response(self):
        from quickbite_users.presenters.get_user_profile_details_presenter import \
            GetUserDetailsPresenter
        presenter = GetUserDetailsPresenter()
        # act
        response = presenter.get_invalid_user_response()
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')

    def test_for_user_profile_details_success_response(self):
        from quickbite_users.presenters.get_user_profile_details_presenter import \
            GetUserDetailsPresenter
        presenter = GetUserDetailsPresenter()
        # arrange
        user_details_dto = UserProfileCompleteDetailsDTOFactory(
            username="user_1",
            email="user1@example.com",
            role="vendor",
            user_id="user_id_1"
        )
        # act
        response = presenter.get_user_profile_details_success_response(
            user_details_dto=user_details_dto)
        # assert
        self.assertMatchSnapshot(json.loads(response.content), 'response_data')
