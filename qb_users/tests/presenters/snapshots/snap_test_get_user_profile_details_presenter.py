# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetUserDetailsPresenter::test_for_invalid_user_response response_data'] = {
    'error': 'User not found'
}

snapshots['TestGetUserDetailsPresenter::test_for_user_profile_details_success_response response_data'] = {
    'email': 'user1@example.com',
    'role': 'vendor',
    'user_id': 'user_id_1',
    'username': 'user_1'
}
