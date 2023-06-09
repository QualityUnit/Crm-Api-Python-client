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
from qu.crm.models.summary_invoice import SummaryInvoice  # noqa: E501
from qu.crm.rest import ApiException

class TestSummaryInvoice(unittest.TestCase):
    """SummaryInvoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SummaryInvoice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SummaryInvoice`
        """
        model = qu.crm.models.summary_invoice.SummaryInvoice()  # noqa: E501
        if include_optional :
            return SummaryInvoice(
                invoice_number = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                paid_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                price_billed = 1.337, 
                currency = 'USD'
            )
        else :
            return SummaryInvoice(
        )
        """

    def testSummaryInvoice(self):
        """Test SummaryInvoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
