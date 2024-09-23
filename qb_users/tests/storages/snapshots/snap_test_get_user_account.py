# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetUserAccount.test_get_user_account_when_username_exists UserAccountDTO(user_id='5de549a4-ece4-4b7d-b0ed-49998f978277', username='user_1', email='user1@example.com', password='password_1')'] = GenericRepr("UserAccountDTO(user_id='5de549a4-ece4-4b7d-b0ed-49998f978277', username='user_1', email='user1@example.com', password='password_1')")
