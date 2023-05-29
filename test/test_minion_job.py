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
from qu.crm.models.minion_job import MinionJob  # noqa: E501
from qu.crm.rest import ApiException

class TestMinionJob(unittest.TestCase):
    """MinionJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MinionJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MinionJob`
        """
        model = qu.crm.models.minion_job.MinionJob()  # noqa: E501
        if include_optional :
            return MinionJob(
                action_id = '', 
                minion_id = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                salt_jid = '', 
                scheduled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                result = 'S', 
                result_body = ''
            )
        else :
            return MinionJob(
                action_id = '',
                minion_id = '',
        )
        """

    def testMinionJob(self):
        """Test MinionJob"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
