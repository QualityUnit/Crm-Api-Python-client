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
from qu.crm.api.liveagent_api import LiveagentApi  # noqa: E501
from qu.crm.rest import ApiException


class TestLiveagentApi(unittest.TestCase):
    """LiveagentApi unit test stubs"""

    def setUp(self):
        self.api = qu.crm.api.liveagent_api.LiveagentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_set_knowledgebases(self):
        """Test case for set_knowledgebases

        Set knowledgebase settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
