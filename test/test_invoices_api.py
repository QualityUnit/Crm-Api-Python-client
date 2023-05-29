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

import qu.crm
from qu.crm.api.invoices_api import InvoicesApi  # noqa: E501
from qu.crm.rest import ApiException


class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

    def setUp(self):
        self.api = qu.crm.api.invoices_api.InvoicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download_invoice(self):
        """Test case for download_invoice

        Download invoice  # noqa: E501
        """
        pass

    def test_get_invoice(self):
        """Test case for get_invoice

        Invoice  # noqa: E501
        """
        pass

    def test_get_invoices(self):
        """Test case for get_invoices

        Invoice list  # noqa: E501
        """
        pass

    def test_refund_invoice(self):
        """Test case for refund_invoice

        Refund invoice  # noqa: E501
        """
        pass

    def test_regenerate_invoice(self):
        """Test case for regenerate_invoice

        Regenerate invoice pdf  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
