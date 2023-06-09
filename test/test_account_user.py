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
import datetime

import qu.crm
from qu.crm.models.account_user import AccountUser  # noqa: E501
from qu.crm.rest import ApiException

class TestAccountUser(unittest.TestCase):
    """AccountUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountUser`
        """
        model = qu.crm.models.account_user.AccountUser()  # noqa: E501
        if include_optional :
            return AccountUser(
                id = '', 
                name = '', 
                email = '', 
                role = '', 
                is_online = True
            )
        else :
            return AccountUser(
        )
        """

    def testAccountUser(self):
        """Test AccountUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
