from rest_framework.decorators import api_view


@api_view(["GET"])
def get_profile_details(request):
    user = request.user
    user_id = user.user_id
    from qb_users.interactors.get_user_profile_datails_interactor import \
        GetUserProfileDetailsInteractor
    from qb_users.storages.user_profile_storage import \
        UserProfileStorage
    from qb_users.presenters.get_user_profile_details_presenter import \
        GetUserDetailsPresenter

    presenter = GetUserDetailsPresenter()
    user_profile_storge = UserProfileStorage()
    interactor = GetUserProfileDetailsInteractor(
        user_profile_storge=user_profile_storge)

    return interactor.get_user_profile_wrapper(user_id=user_id, presenter=presenter)


