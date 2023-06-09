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
from qu.crm.models.custom_domain import CustomDomain  # noqa: E501
from qu.crm.rest import ApiException

class TestCustomDomain(unittest.TestCase):
    """CustomDomain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CustomDomain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomDomain`
        """
        model = qu.crm.models.custom_domain.CustomDomain()  # noqa: E501
        if include_optional :
            return CustomDomain(
                custom_domain = '', 
                ssl_key = '', 
                ssl_crt = ''
            )
        else :
            return CustomDomain(
        )
        """

    def testCustomDomain(self):
        """Test CustomDomain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
