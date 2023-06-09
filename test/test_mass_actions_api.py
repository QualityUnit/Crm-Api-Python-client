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
from qu.crm.api.mass_actions_api import MassActionsApi  # noqa: E501
from qu.crm.rest import ApiException


class TestMassActionsApi(unittest.TestCase):
    """MassActionsApi unit test stubs"""

    def setUp(self):
        self.api = qu.crm.api.mass_actions_api.MassActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mass_delete(self):
        """Test case for mass_delete

        Delete multiple subscriptions  # noqa: E501
        """
        pass

    def test_mass_suspend(self):
        """Test case for mass_suspend

        Suspend multiple subscriptions  # noqa: E501
        """
        pass

    def test_mass_terminate(self):
        """Test case for mass_terminate

        Terminate multiple subscriptions  # noqa: E501
        """
        pass

    def test_mass_update(self):
        """Test case for mass_update

        Update multiple subscriptions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
