# coding: utf-8

"""
    CRM API

    This page contains complete API documentation for CRM software.  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: support@qualityunit.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import qu.crm
from qu.crm.api.settings_api import SettingsApi  # noqa: E501
from qu.crm.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = qu.crm.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_settings(self):
        """Test case for get_settings

        Settings list  # noqa: E501
        """
        pass

    def test_update_setting_group(self):
        """Test case for update_setting_group

        Update setting group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
