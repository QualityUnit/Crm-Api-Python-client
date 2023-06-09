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
from qu.crm.models.version_name import VersionName  # noqa: E501
from qu.crm.rest import ApiException

class TestVersionName(unittest.TestCase):
    """VersionName unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VersionName
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VersionName`
        """
        model = qu.crm.models.version_name.VersionName()  # noqa: E501
        if include_optional :
            return VersionName(
                id = '', 
                name = '', 
                is_stable = True
            )
        else :
            return VersionName(
        )
        """

    def testVersionName(self):
        """Test VersionName"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
