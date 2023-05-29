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
from qu.crm.models.credentials import Credentials  # noqa: E501
from qu.crm.rest import ApiException

class TestCredentials(unittest.TestCase):
    """Credentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Credentials
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Credentials`
        """
        model = qu.crm.models.credentials.Credentials()  # noqa: E501
        if include_optional :
            return Credentials(
                username = '', 
                password = ''
            )
        else :
            return Credentials(
                username = '',
                password = '',
        )
        """

    def testCredentials(self):
        """Test Credentials"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()