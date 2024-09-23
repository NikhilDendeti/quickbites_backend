# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestSigninUserPresenter.test_for_invalid_password_response response_data'] = {
    'error': 'Invalid Password'
}

snapshots['TestSigninUserPresenter.test_for_success_response response_data'] = {
    'access_token': 'access_toekn_1',
    'expires_in': 100,
    'refresh_token': 'refresh_token_1',
    'user_id': 'user_id_1'
}

snapshots['TestSigninUserPresenter.test_for_username_does_not_exists_response response_data'] = {
    'error': 'User Name Not Exist'
}
