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
from qu.crm.models.reseller_signup import ResellerSignup  # noqa: E501
from qu.crm.rest import ApiException

class TestResellerSignup(unittest.TestCase):
    """ResellerSignup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResellerSignup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResellerSignup`
        """
        model = qu.crm.models.reseller_signup.ResellerSignup()  # noqa: E501
        if include_optional :
            return ResellerSignup(
                variation_id = '', 
                subdomain = '', 
                initial_name = '', 
                initial_email = '', 
                initial_pass = '', 
                initial_language = '', 
                initial_api_key = ''
            )
        else :
            return ResellerSignup(
                variation_id = '',
                subdomain = '',
                initial_name = '',
                initial_email = '',
        )
        """

    def testResellerSignup(self):
        """Test ResellerSignup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
