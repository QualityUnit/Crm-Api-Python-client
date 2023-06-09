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
from qu.crm.models.variation_upgrade import VariationUpgrade  # noqa: E501
from qu.crm.rest import ApiException

class TestVariationUpgrade(unittest.TestCase):
    """VariationUpgrade unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VariationUpgrade
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariationUpgrade`
        """
        model = qu.crm.models.variation_upgrade.VariationUpgrade()  # noqa: E501
        if include_optional :
            return VariationUpgrade(
                variation = qu.crm.models.variation.Variation(
                    id = '', 
                    billable = True, 
                    name = '', 
                    product_id = '', 
                    product_name = '', 
                    full_name = '', 
                    description = '', 
                    limits = qu.crm.models.limits.limits(), ), 
                addons = [
                    qu.crm.models.addon.Addon(
                        codename = '', 
                        name = '', 
                        description = '', 
                        state = '', 
                        price = 56, 
                        active = True, )
                    ], 
                billing_periods = [
                    qu.crm.models.period_pricing.PeriodPricing(
                        name = '1m', 
                        metrics = [
                            qu.crm.models.billing_metric.BillingMetric(
                                name = '', 
                                amount_in_price = 56, 
                                limit = 56, 
                                unit_price = 1.337, 
                                unit_size = 56, )
                            ], 
                        base_price = 56, )
                    ], 
                metrics = [
                    qu.crm.models.billing_metric.BillingMetric(
                        name = '', 
                        amount_in_price = 56, 
                        limit = 56, 
                        unit_price = 1.337, 
                        unit_size = 56, )
                    ], 
                base_price = 56, 
                discounts = [
                    qu.crm.models.discount_value.DiscountValue(
                        name = '', 
                        type = 'one_time', 
                        value_type = 'per_cent', 
                        value = 56, )
                    ]
            )
        else :
            return VariationUpgrade(
        )
        """

    def testVariationUpgrade(self):
        """Test VariationUpgrade"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
