# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateUserPresenter.test_for_invalid_email response_data'] = {
    'error': 'Incorrect Mail Format'
}

snapshots['TestCreateUserPresenter.test_for_invalid_password_format response_data'] = {
    'error': '''message1
message2'''
}

snapshots['TestCreateUserPresenter.test_for_invalid_user_name_format response_data'] = {
    'error': 'Invalid User Name Format'
}

snapshots['TestCreateUserPresenter.test_for_invalid_user_name_length response_data'] = {
    'error': 'Invalid User Name Length'
}

snapshots['TestCreateUserPresenter.test_for_success_case response_data'] = {
    'access_token': 'access_toekn_1',
    'expires_in': '100',
    'refresh_token': 'refresh_token_1',
    'user_id': 'user_id_1'
}

snapshots['TestCreateUserPresenter.test_for_token_generation_failed response_data'] = {
    'error': 'Token generation failed'
}

snapshots['TestCreateUserPresenter.test_for_user_already_exist response_data'] = {
    'error': 'User Already Exist'
}

snapshots['TestCreateUserPresenter::test_for_invalid_email response_data'] = {
    'error': 'Incorrect Mail Format'
}

snapshots['TestCreateUserPresenter::test_for_invalid_password_format response_data'] = {
    'error': '''message1
message2'''
}

snapshots['TestCreateUserPresenter::test_for_invalid_user_name_format response_data'] = {
    'error': 'Invalid User Name Format'
}

snapshots['TestCreateUserPresenter::test_for_invalid_user_name_length response_data'] = {
    'error': 'Invalid User Name Length'
}

snapshots['TestCreateUserPresenter::test_for_success_case response_data'] = {
    'access_token': 'access_toekn_1',
    'expires_in': '100',
    'refresh_token': 'refresh_token_1',
    'user_id': 'user_id_1'
}

snapshots['TestCreateUserPresenter::test_for_token_generation_failed response_data'] = {
    'error': 'Token generation failed'
}

snapshots['TestCreateUserPresenter::test_for_user_already_exist response_data'] = {
    'error': 'User Already Exist'
}
