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
from qu.crm.models.my_account_parameters import MyAccountParameters  # noqa: E501
from qu.crm.rest import ApiException

class TestMyAccountParameters(unittest.TestCase):
    """MyAccountParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MyAccountParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MyAccountParameters`
        """
        model = qu.crm.models.my_account_parameters.MyAccountParameters()  # noqa: E501
        if include_optional :
            return MyAccountParameters(
                variation_id = '', 
                addons = '', 
                agents_count = '', 
                knowledgebase_count = '', 
                entry_point = '', 
                is_standalone = True
            )
        else :
            return MyAccountParameters(
                entry_point = '',
        )
        """

    def testMyAccountParameters(self):
        """Test MyAccountParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()