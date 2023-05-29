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
from qu.crm.models.range_value import RangeValue  # noqa: E501
from qu.crm.rest import ApiException

class TestRangeValue(unittest.TestCase):
    """RangeValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RangeValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RangeValue`
        """
        model = qu.crm.models.range_value.RangeValue()  # noqa: E501
        if include_optional :
            return RangeValue(
                from_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                to_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                value = 56
            )
        else :
            return RangeValue(
        )
        """

    def testRangeValue(self):
        """Test RangeValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
