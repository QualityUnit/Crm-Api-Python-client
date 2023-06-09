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
from qu.crm.models.subscription_view_data import SubscriptionViewData  # noqa: E501
from qu.crm.rest import ApiException

class TestSubscriptionViewData(unittest.TestCase):
    """SubscriptionViewData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionViewData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionViewData`
        """
        model = qu.crm.models.subscription_view_data.SubscriptionViewData()  # noqa: E501
        if include_optional :
            return SubscriptionViewData(
                addons = [
                    qu.crm.models.addon.Addon(
                        codename = '', 
                        name = '', 
                        description = '', 
                        state = '', 
                        price = 56, 
                        active = True, )
                    ], 
                billing_status = qu.crm.models.billing_status.BillingStatus(
                    status = 'N', 
                    valid_to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_billing_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    billing_day = 56, 
                    billing_period = '1m', 
                    billing_period_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    billing_period_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    errors = 56, 
                    last_error_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    payment_compatible = True, 
                    uses_legacy_billing = True, ), 
                customer = qu.crm.models.customer.Customer(
                    name = '', 
                    email = '', 
                    company = '', 
                    phone = '', 
                    address1 = '', 
                    address2 = '', 
                    city = '', 
                    state = '', 
                    country = '', 
                    zip = '', 
                    vat_id = '', 
                    ico_sk = '', 
                    dic_sk = '', ), 
                domain = qu.crm.models.domain.Domain(
                    domain = '', 
                    custom_domain = '', 
                    ssl_key = '', 
                    ssl_crt = '', ), 
                note = qu.crm.models.note.Note(
                    note = '', ), 
                source = qu.crm.models.source.Source(
                    source_id = '', ), 
                variation_addons = [
                    qu.crm.models.addon.Addon(
                        codename = '', 
                        name = '', 
                        description = '', 
                        state = '', 
                        price = 56, 
                        active = True, )
                    ], 
                account_manager = qu.crm.models.account_manager.AccountManager(
                    account_manager = '', ), 
                db = qu.crm.models.subscription_view_db.SubscriptionViewDb(
                    hostname = '', 
                    host = '', 
                    port = '', 
                    user = '', 
                    pass = '', ), 
                version_info = qu.crm.models.version_info.VersionInfo(
                    latest_stable = '', 
                    latest_available = '', 
                    latest_candidate = '', 
                    is_available = True, 
                    is_stable = True, 
                    is_candidate = True, ), 
                locks = [
                    ''
                    ], 
                initial_login_attempts = qu.crm.models.initial_login_attempts.InitialLoginAttempts(
                    initial_login_attempts = '', ), 
                initial_lang = qu.crm.models.initial_lang.InitialLang(
                    initial_lang = '', ), 
                public_ip = qu.crm.models.public_ip.PublicIp(
                    public_ip = '', ), 
                score = qu.crm.models.score.Score(
                    score = '', ), 
                owner_email = qu.crm.models.owner_email.OwnerEmail(
                    owner_email = '', ), 
                asterisk_host = qu.crm.models.asterisk_host.AsteriskHost(
                    asterisk_host = '', ), 
                aws_region = qu.crm.models.aws_region.AwsRegion(
                    aws_region = '', ), 
                track_ga_client = qu.crm.models.track_ga_client.TrackGaClient(
                    track_ga_client_id = '', ), 
                track_pap_signup_ip = qu.crm.models.track_pap_signup_ip.TrackPapSignupIp(
                    track_pap_signup_ip = '', ), 
                track_pap_user_agent = qu.crm.models.track_pap_user_agent.TrackPapUserAgent(
                    track_pap_user_agent = '', ), 
                hosted_api_key = qu.crm.models.hosted_api_key.HostedApiKey(
                    hosted_api_key = '', )
            )
        else :
            return SubscriptionViewData(
        )
        """

    def testSubscriptionViewData(self):
        """Test SubscriptionViewData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
