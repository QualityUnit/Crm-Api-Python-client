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
from qu.crm.models.billing_parameters import BillingParameters  # noqa: E501
from qu.crm.rest import ApiException

class TestBillingParameters(unittest.TestCase):
    """BillingParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BillingParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingParameters`
        """
        model = qu.crm.models.billing_parameters.BillingParameters()  # noqa: E501
        if include_optional :
            return BillingParameters(
                billing_period = '1m', 
                variation_id = '', 
                addons = [
                    ''
                    ], 
                coupon = ''
            )
        else :
            return BillingParameters(
        )
        """

    def testBillingParameters(self):
        """Test BillingParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
