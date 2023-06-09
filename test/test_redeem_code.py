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
from qu.crm.models.redeem_code import RedeemCode  # noqa: E501
from qu.crm.rest import ApiException

class TestRedeemCode(unittest.TestCase):
    """RedeemCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RedeemCode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RedeemCode`
        """
        model = qu.crm.models.redeem_code.RedeemCode()  # noqa: E501
        if include_optional :
            return RedeemCode(
                code = '', 
                variation_id = '', 
                expires_at = '', 
                discount_template = qu.crm.models.discount_template.DiscountTemplate(
                    type = 'one_time', 
                    value_type = 'constant', 
                    value = 56, 
                    days_valid = 56, 
                    name = '', ), 
                redemption = qu.crm.models.redemption.Redemption(
                    redeemer_name = '', 
                    redeemer_email = '', 
                    redeemed_at = '', 
                    subscription_id = '', )
            )
        else :
            return RedeemCode(
                code = '',
                variation_id = '',
        )
        """

    def testRedeemCode(self):
        """Test RedeemCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
