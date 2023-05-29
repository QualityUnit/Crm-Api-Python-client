# qu.crm
This page contains complete API documentation for CRM software.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/qualityunit/Crm-Api-Python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/qualityunit/Crm-Api-Python-client.git`)

Then import the package:
```python
import qu.crm
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import qu.crm
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import qu.crm
from qu.crm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://crm.qualityunit.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = qu.crm.Configuration(
    host = "https://crm.qualityunit.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.AdminPanelApi(api_client)

    try:
        # Subscription source list
        api_response = await api_instance.get_subscription_sources()
        print("The response of AdminPanelApi->get_subscription_sources:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminPanelApi->get_subscription_sources: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminPanelApi* | [**get_subscription_sources**](docs/AdminPanelApi.md#get_subscription_sources) | **GET** /admin_panel/sources | Subscription source list
*AdminPanelApi* | [**get_subscription_view**](docs/AdminPanelApi.md#get_subscription_view) | **GET** /admin_panel/subscription_view/{subscriptionId} | Subscription view data
*AttributesApi* | [**get_attribute**](docs/AttributesApi.md#get_attribute) | **GET** /attributes/{attributeId} | Attribute
*AttributesApi* | [**get_attributes**](docs/AttributesApi.md#get_attributes) | **GET** /attributes | Attribute list
*AttributesApi* | [**set_attribute**](docs/AttributesApi.md#set_attribute) | **PUT** /attributes/{attributeId} | Attribute
*BillingApi* | [**check_vat**](docs/BillingApi.md#check_vat) | **POST** /billing/_check_vat | Vat validity
*CountriesApi* | [**get_countries**](docs/CountriesApi.md#get_countries) | **GET** /countries | Country list
*CouponApi* | [**get_coupon**](docs/CouponApi.md#get_coupon) | **GET** /coupons/{couponCode} | Coupon
*CouponsApi* | [**extend_coupon_validity**](docs/CouponsApi.md#extend_coupon_validity) | **POST** /coupons/{couponCode}/_extend_validity | Extend coupon validity
*DevApi* | [**dev_create_subscription**](docs/DevApi.md#dev_create_subscription) | **POST** /dev/_create_subscription | Create dev subscription
*EventLogsApi* | [**get_event_logs**](docs/EventLogsApi.md#get_event_logs) | **GET** /event_logs | Event logs list
*HackApi* | [**hack_dummy_payment_method**](docs/HackApi.md#hack_dummy_payment_method) | **POST** /_hack/_dummy_payment_method | Set dummy payment method
*InternalApi* | [**account_user_login**](docs/InternalApi.md#account_user_login) | **GET** /subscriptions/{subscriptionId}/_login | Login as account user
*InternalApi* | [**cancel_discount**](docs/InternalApi.md#cancel_discount) | **DELETE** /discounts/{discountId} | Cancel discount
*InternalApi* | [**create_coupon**](docs/InternalApi.md#create_coupon) | **POST** /coupons | Create coupon
*InternalApi* | [**create_discount**](docs/InternalApi.md#create_discount) | **POST** /discounts | Create discount
*InternalApi* | [**custom_reseller_url**](docs/InternalApi.md#custom_reseller_url) | **GET** /subscriptions/{subscriptionId}/upgrade_url | Custom reseller upgrade URL
*InternalApi* | [**elastic_reindex**](docs/InternalApi.md#elastic_reindex) | **POST** /subscriptions/{subscriptionId}/elastic_reindex | Elastic reindex subscription LA data
*InternalApi* | [**elastic_reindex_status**](docs/InternalApi.md#elastic_reindex_status) | **GET** /subscriptions/{subscriptionId}/elastic_status | LA elastic reindex status
*InternalApi* | [**generate_for_agents**](docs/InternalApi.md#generate_for_agents) | **POST** /my-account/{subscriptionId}/_authorize | &#39;My Account&#39; token
*InternalApi* | [**get_account_users**](docs/InternalApi.md#get_account_users) | **GET** /subscriptions/{subscriptionId}/account_users | Account users
*InternalApi* | [**get_coupons**](docs/InternalApi.md#get_coupons) | **GET** /coupons | Coupons list
*InternalApi* | [**get_discount**](docs/InternalApi.md#get_discount) | **GET** /discounts/{discountId} | Discount
*InternalApi* | [**get_discounts**](docs/InternalApi.md#get_discounts) | **GET** /discounts | Discount list
*InternalApi* | [**get_outbox_email**](docs/InternalApi.md#get_outbox_email) | **GET** /outbox/{emailId} | Email
*InternalApi* | [**get_outbox_emails**](docs/InternalApi.md#get_outbox_emails) | **GET** /outbox | Email list
*InternalApi* | [**get_subscription_status_history**](docs/InternalApi.md#get_subscription_status_history) | **GET** /subscriptions/{subscriptionId}/status_history | Status history
*InternalApi* | [**get_usage_breakdown**](docs/InternalApi.md#get_usage_breakdown) | **GET** /subscriptions/{subscriptionId}/__usage_breakdown | Show usage breakdown
*InvoicesApi* | [**download_invoice**](docs/InvoicesApi.md#download_invoice) | **GET** /invoices/{invoiceNumber}/_download | Download invoice
*InvoicesApi* | [**get_invoice**](docs/InvoicesApi.md#get_invoice) | **GET** /invoices/{invoiceNumber} | Invoice
*InvoicesApi* | [**get_invoices**](docs/InvoicesApi.md#get_invoices) | **GET** /invoices | Invoice list
*InvoicesApi* | [**refund_invoice**](docs/InvoicesApi.md#refund_invoice) | **POST** /invoices/{invoiceNumber}/_refund | Refund invoice
*InvoicesApi* | [**regenerate_invoice**](docs/InvoicesApi.md#regenerate_invoice) | **POST** /invoices/{invoiceNumber}/_regenerate_pdf | Regenerate invoice pdf
*LakbdomainApi* | [**check_certificate**](docs/LakbdomainApi.md#check_certificate) | **PUT** /lakbdomain/_check_certificate | Certificate check
*LiveagentApi* | [**set_knowledgebases**](docs/LiveagentApi.md#set_knowledgebases) | **POST** /subscriptions/{subscriptionId}/liveagent/knowledgebases | Set knowledgebase settings
*MassActionsApi* | [**mass_delete**](docs/MassActionsApi.md#mass_delete) | **POST** /subscriptions/massAction/_delete | Delete multiple subscriptions
*MassActionsApi* | [**mass_suspend**](docs/MassActionsApi.md#mass_suspend) | **POST** /subscriptions/massAction/_suspend | Suspend multiple subscriptions
*MassActionsApi* | [**mass_terminate**](docs/MassActionsApi.md#mass_terminate) | **POST** /subscriptions/massAction/_terminate | Terminate multiple subscriptions
*MassActionsApi* | [**mass_update**](docs/MassActionsApi.md#mass_update) | **POST** /subscriptions/massAction/_update | Update multiple subscriptions
*MinionsApi* | [**add_new_minion**](docs/MinionsApi.md#add_new_minion) | **POST** /minions | Add new minion
*MinionsApi* | [**delete_minion**](docs/MinionsApi.md#delete_minion) | **DELETE** /minions/{minionId} | Delete minion
*MinionsApi* | [**edit_minion**](docs/MinionsApi.md#edit_minion) | **PUT** /minions/{minionId} | Edit minion
*MinionsApi* | [**get_minion**](docs/MinionsApi.md#get_minion) | **GET** /minions/{minionId} | Minion
*MinionsApi* | [**get_minion_cluster_names**](docs/MinionsApi.md#get_minion_cluster_names) | **GET** /minions/options/clusterNames | Minion cluster names list
*MinionsApi* | [**get_minion_roles**](docs/MinionsApi.md#get_minion_roles) | **GET** /minions/options/roles | Minion roles list
*MinionsApi* | [**get_minions**](docs/MinionsApi.md#get_minions) | **GET** /minions | Minions list
*MinionsApi* | [**re_sync_minion**](docs/MinionsApi.md#re_sync_minion) | **POST** /minions/{minionId}/_reSync | Resync minion and set it up
*MinionsApi* | [**set_minion_down**](docs/MinionsApi.md#set_minion_down) | **POST** /minions/{minionId}/_setDown | Set minion down
*MinionsApi* | [**set_minion_up**](docs/MinionsApi.md#set_minion_up) | **POST** /minions/{minionId}/_setUp | Set minion up
*MyAccountApi* | [**cancel_stop**](docs/MyAccountApi.md#cancel_stop) | **POST** /my-account/_cancelStop | Restart billing
*MyAccountApi* | [**change_addons_for_my_account**](docs/MyAccountApi.md#change_addons_for_my_account) | **PUT** /my-account/addons | Addon change
*MyAccountApi* | [**download_invoice_for_my_account**](docs/MyAccountApi.md#download_invoice_for_my_account) | **GET** /my-account/invoices/{invoiceNumber}/_download | Download invoice
*MyAccountApi* | [**download_summary**](docs/MyAccountApi.md#download_summary) | **GET** /my-account/summary/{orderNumber}/_download | Downloads summary
*MyAccountApi* | [**generate**](docs/MyAccountApi.md#generate) | **POST** /checkout/_authorize | &#39;My Account&#39; token
*MyAccountApi* | [**get_account_invoices**](docs/MyAccountApi.md#get_account_invoices) | **GET** /my-account/invoices | Invoices list
*MyAccountApi* | [**get_account_summaries**](docs/MyAccountApi.md#get_account_summaries) | **GET** /my-account/summary/history | Summaries list
*MyAccountApi* | [**get_active_addons_for_my_account**](docs/MyAccountApi.md#get_active_addons_for_my_account) | **GET** /my-account/addons | Plan addons list
*MyAccountApi* | [**get_agents_count**](docs/MyAccountApi.md#get_agents_count) | **GET** /my-account/usage/agents/count | Agents count
*MyAccountApi* | [**get_all_variation_addons_for_my_account**](docs/MyAccountApi.md#get_all_variation_addons_for_my_account) | **GET** /my-account/variations/{variationId}/addons | Variations addons
*MyAccountApi* | [**get_billing_info_for_my_account**](docs/MyAccountApi.md#get_billing_info_for_my_account) | **GET** /my-account/billingInfo | Billing info
*MyAccountApi* | [**get_billing_status_for_my_account**](docs/MyAccountApi.md#get_billing_status_for_my_account) | **GET** /my-account/billingStatus | Billing status
*MyAccountApi* | [**get_coupon_for_my_account**](docs/MyAccountApi.md#get_coupon_for_my_account) | **GET** /my-account/coupons/{couponCode} | Coupon
*MyAccountApi* | [**get_knowledgebases_count**](docs/MyAccountApi.md#get_knowledgebases_count) | **GET** /my-account/usage/knowledgebases/count | Knowledgebases count
*MyAccountApi* | [**get_payment_method_for_my_account**](docs/MyAccountApi.md#get_payment_method_for_my_account) | **GET** /my-account/paymentMethod | Get Payment method
*MyAccountApi* | [**get_payment_processor_for_my_account**](docs/MyAccountApi.md#get_payment_processor_for_my_account) | **GET** /my-account/paymentProcessor | Payment processor
*MyAccountApi* | [**get_subscription_for_my_account**](docs/MyAccountApi.md#get_subscription_for_my_account) | **GET** /my-account/subscription | Subscription
*MyAccountApi* | [**get_summary_for_my_account**](docs/MyAccountApi.md#get_summary_for_my_account) | **GET** /my-account/summary | Current period summary
*MyAccountApi* | [**get_upgrade_variations_for_my_account**](docs/MyAccountApi.md#get_upgrade_variations_for_my_account) | **GET** /my-account/upgradeVariations | Upgrade variation list
*MyAccountApi* | [**get_variation_for_my_account**](docs/MyAccountApi.md#get_variation_for_my_account) | **GET** /my-account/variation | Variation
*MyAccountApi* | [**parameters**](docs/MyAccountApi.md#parameters) | **GET** /my-account/parameters | &#39;My Account&#39; parameters
*MyAccountApi* | [**predict_price**](docs/MyAccountApi.md#predict_price) | **POST** /my-account/_predictPrice | Returns list of items and predicted price
*MyAccountApi* | [**send_payment_error**](docs/MyAccountApi.md#send_payment_error) | **POST** /my-account/sendPaymentError | Sends payment error to server
*MyAccountApi* | [**stop_account**](docs/MyAccountApi.md#stop_account) | **POST** /my-account/_stop | Stop billing
*MyAccountApi* | [**update_billing_info**](docs/MyAccountApi.md#update_billing_info) | **PUT** /my-account/billingInfo | Billing info
*MyAccountApi* | [**update_payment_method**](docs/MyAccountApi.md#update_payment_method) | **PUT** /my-account/paymentMethod | Update payment method
*MyAccountApi* | [**upgrade_plan**](docs/MyAccountApi.md#upgrade_plan) | **POST** /my-account/_upgrade | Change plan
*MyAccountApi* | [**validate_billing_info_for_my_account**](docs/MyAccountApi.md#validate_billing_info_for_my_account) | **POST** /my-account/_validateBillingInfo | Test Billing info
*ProductsApi* | [**create_product_version**](docs/ProductsApi.md#create_product_version) | **POST** /products/{productId}/versions | Create new product version
*ProductsApi* | [**delete_product_version**](docs/ProductsApi.md#delete_product_version) | **DELETE** /products/{productId}/versions/{productVersionName} | Delete product version
*ProductsApi* | [**get_all_product_available_versions**](docs/ProductsApi.md#get_all_product_available_versions) | **GET** /products/{productId}/available_versions | Product available versions
*ProductsApi* | [**get_product**](docs/ProductsApi.md#get_product) | **GET** /products/{productId} | Product
*ProductsApi* | [**get_product_version**](docs/ProductsApi.md#get_product_version) | **GET** /products/{productId}/versions/{productVersionName} | Product version
*ProductsApi* | [**get_product_versions**](docs/ProductsApi.md#get_product_versions) | **GET** /products/{productId}/versions | Product versions
*ProductsApi* | [**get_products**](docs/ProductsApi.md#get_products) | **GET** /products | Products list
*ProductsApi* | [**mark_product_version_for_deletion**](docs/ProductsApi.md#mark_product_version_for_deletion) | **PUT** /products/{productId}/versions/{productVersionName}/mark_for_deletion | Mark product version for deletion
*ProductsApi* | [**update_product_version**](docs/ProductsApi.md#update_product_version) | **PUT** /products/{productId}/versions/{productVersionName} | Update product version
*RedeemCodesApi* | [**create_redeem_code**](docs/RedeemCodesApi.md#create_redeem_code) | **POST** /redeem_codes | Create redeem code
*RedeemCodesApi* | [**get_redeem_code**](docs/RedeemCodesApi.md#get_redeem_code) | **GET** /redeem_codes/{redeemCode} | Redeem code
*RedeemCodesApi* | [**get_redeem_codes**](docs/RedeemCodesApi.md#get_redeem_codes) | **GET** /redeem_codes | Redeem codes list
*RedeemCodesApi* | [**redeem_code_signup**](docs/RedeemCodesApi.md#redeem_code_signup) | **POST** /redeem_code/signup | Create subscription
*RedeemCodesApi* | [**redeem_codes_import**](docs/RedeemCodesApi.md#redeem_codes_import) | **POST** /redeem_codes/import | Import redeem codes
*RefundsApi* | [**get_refund**](docs/RefundsApi.md#get_refund) | **GET** /refunds/{refundId} | Refund
*RefundsApi* | [**get_refunds**](docs/RefundsApi.md#get_refunds) | **GET** /refunds | Refund list
*ResellerApi* | [**get_reseller_billed_periods**](docs/ResellerApi.md#get_reseller_billed_periods) | **GET** /reseller/subscriptions/{subscriptionId}/billed_periods | Reseller subscription billed period list
*ResellerApi* | [**get_reseller_invoices**](docs/ResellerApi.md#get_reseller_invoices) | **GET** /reseller/invoices | Reseller invoice list
*ResellerApi* | [**get_reseller_subscription**](docs/ResellerApi.md#get_reseller_subscription) | **GET** /reseller/subscriptions/{subscriptionId} | Get reseller subscription
*ResellerApi* | [**get_reseller_subscription_usage**](docs/ResellerApi.md#get_reseller_subscription_usage) | **GET** /reseller/subscriptions/{subscriptionId}/usage/agents | Get reseller subscription usage
*ResellerApi* | [**get_reseller_subscriptions**](docs/ResellerApi.md#get_reseller_subscriptions) | **GET** /reseller/subscriptions | Get reseller subscriptions
*ResellerApi* | [**reseller_change_plan**](docs/ResellerApi.md#reseller_change_plan) | **POST** /reseller/subscriptions/{subscriptionId}/_upgrade | Change plan
*ResellerApi* | [**reseller_signup**](docs/ResellerApi.md#reseller_signup) | **POST** /reseller/subscriptions | Create reseller subscription
*ResellerApi* | [**suspend_reseller_subscription**](docs/ResellerApi.md#suspend_reseller_subscription) | **POST** /reseller/subscriptions/{subscriptionId}/_suspend | Suspend reseller subscription
*ResellerApi* | [**unsuspend_reseller_subscription**](docs/ResellerApi.md#unsuspend_reseller_subscription) | **POST** /reseller/subscriptions/{subscriptionId}/_unsuspend | Unsuspend reseller subscription
*SettingsApi* | [**get_settings**](docs/SettingsApi.md#get_settings) | **GET** /settings | Settings list
*SettingsApi* | [**update_setting_group**](docs/SettingsApi.md#update_setting_group) | **PUT** /settings | Update setting group
*StatsApi* | [**get_account_stats**](docs/StatsApi.md#get_account_stats) | **GET** /stats/account | Account stats
*StatsApi* | [**get_agents_stats**](docs/StatsApi.md#get_agents_stats) | **GET** /stats/agents | Agents stats for accounts with 10 or more agents
*StatsApi* | [**get_sale_stats**](docs/StatsApi.md#get_sale_stats) | **GET** /stats/sale | Sale stats
*StatsApi* | [**get_versions_stats**](docs/StatsApi.md#get_versions_stats) | **GET** /stats/versions | Versions stats
*SubscriptionsApi* | [**add_free_addons**](docs/SubscriptionsApi.md#add_free_addons) | **POST** /subscriptions/{subscriptionId}/_addFreeAddons | Add free addons
*SubscriptionsApi* | [**aet_account_manager**](docs/SubscriptionsApi.md#aet_account_manager) | **PUT** /subscriptions/{subscriptionId}/account_manager | Assign account manager
*SubscriptionsApi* | [**agree_with_request_billing**](docs/SubscriptionsApi.md#agree_with_request_billing) | **POST** /subscriptions/{subscriptionId}/pap_request_billing | PAP agree with additional billing
*SubscriptionsApi* | [**change_addons**](docs/SubscriptionsApi.md#change_addons) | **PUT** /subscriptions/{subscriptionId}/addons | Addon change
*SubscriptionsApi* | [**change_plan**](docs/SubscriptionsApi.md#change_plan) | **POST** /subscriptions/{subscriptionId}/_upgrade | Change plan
*SubscriptionsApi* | [**check_domain**](docs/SubscriptionsApi.md#check_domain) | **POST** /subscriptions/_check_domain | Domain availability
*SubscriptionsApi* | [**clear_last_payment_fail**](docs/SubscriptionsApi.md#clear_last_payment_fail) | **POST** /subscriptions/{subscriptionId}/_clearLastPaymentFail | Clear last payment fail
*SubscriptionsApi* | [**delete**](docs/SubscriptionsApi.md#delete) | **POST** /subscriptions/{subscriptionId}/_delete | Delete subscription
*SubscriptionsApi* | [**extend_validity**](docs/SubscriptionsApi.md#extend_validity) | **POST** /subscriptions/{subscriptionId}/_extendValidity | Extends account validity
*SubscriptionsApi* | [**get_account**](docs/SubscriptionsApi.md#get_account) | **GET** /accounts/{accountId} | Account
*SubscriptionsApi* | [**get_account_manager**](docs/SubscriptionsApi.md#get_account_manager) | **GET** /subscriptions/{subscriptionId}/account_manager | Get account manager
*SubscriptionsApi* | [**get_active_addons**](docs/SubscriptionsApi.md#get_active_addons) | **GET** /subscriptions/{subscriptionId}/addons | Addon list
*SubscriptionsApi* | [**get_billing_info**](docs/SubscriptionsApi.md#get_billing_info) | **GET** /subscriptions/{subscriptionId}/billingInfo | Billing info
*SubscriptionsApi* | [**get_billing_metrics**](docs/SubscriptionsApi.md#get_billing_metrics) | **GET** /subscriptions/{subscriptionId}/billingMetrics | Billing metrics
*SubscriptionsApi* | [**get_billing_status**](docs/SubscriptionsApi.md#get_billing_status) | **GET** /subscriptions/{subscriptionId}/billingStatus | Billing status
*SubscriptionsApi* | [**get_domain_info**](docs/SubscriptionsApi.md#get_domain_info) | **GET** /subscriptions/{subscriptionId}/domain | Domain info
*SubscriptionsApi* | [**get_failed_payment**](docs/SubscriptionsApi.md#get_failed_payment) | **GET** /failed_payments/{failedPaymentId} | Failed payment
*SubscriptionsApi* | [**get_failed_payments**](docs/SubscriptionsApi.md#get_failed_payments) | **GET** /failed_payments | Failed payment list
*SubscriptionsApi* | [**get_install_progress**](docs/SubscriptionsApi.md#get_install_progress) | **GET** /subscriptions/{subscriptionId}/install_progress | Install progress
*SubscriptionsApi* | [**get_note**](docs/SubscriptionsApi.md#get_note) | **GET** /subscriptions/{subscriptionId}/note | Note
*SubscriptionsApi* | [**get_payment_method**](docs/SubscriptionsApi.md#get_payment_method) | **GET** /subscriptions/{subscriptionId}/paymentMethod | Payment method
*SubscriptionsApi* | [**get_payment_processor**](docs/SubscriptionsApi.md#get_payment_processor) | **GET** /subscriptions/{subscriptionId}/paymentProcessor | Payment processor
*SubscriptionsApi* | [**get_source**](docs/SubscriptionsApi.md#get_source) | **GET** /subscriptions/{subscriptionId}/source | Install source
*SubscriptionsApi* | [**get_subscription**](docs/SubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription
*SubscriptionsApi* | [**get_subscription_attributes**](docs/SubscriptionsApi.md#get_subscription_attributes) | **GET** /subscriptions/{subscriptionId}/attributes | Subscription attribute list
*SubscriptionsApi* | [**get_subscription_discounts**](docs/SubscriptionsApi.md#get_subscription_discounts) | **GET** /subscriptions/{subscriptionId}/discounts | Subscription discounts
*SubscriptionsApi* | [**get_subscription_invoices**](docs/SubscriptionsApi.md#get_subscription_invoices) | **GET** /subscriptions/{subscriptionId}/invoices | Subscription invoice list
*SubscriptionsApi* | [**get_subscriptions**](docs/SubscriptionsApi.md#get_subscriptions) | **GET** /subscriptions | Subscription list
*SubscriptionsApi* | [**get_upgrade_variations**](docs/SubscriptionsApi.md#get_upgrade_variations) | **GET** /subscriptions/{subscriptionId}/upgradeVariations | Upgrade variation list
*SubscriptionsApi* | [**is_additional_billing_agreed**](docs/SubscriptionsApi.md#is_additional_billing_agreed) | **GET** /subscriptions/{subscriptionId}/pap_request_billing | PAP get additional billing
*SubscriptionsApi* | [**refresh_account**](docs/SubscriptionsApi.md#refresh_account) | **POST** /subscriptions/{subscriptionId}/_refreshAccount | Refresh account
*SubscriptionsApi* | [**remove_lock**](docs/SubscriptionsApi.md#remove_lock) | **PUT** /subscriptions/{subscriptionId}/unlock | Remove lock
*SubscriptionsApi* | [**resume_billing**](docs/SubscriptionsApi.md#resume_billing) | **POST** /subscriptions/{subscriptionId}/_cancelStop | Restart billing
*SubscriptionsApi* | [**set_billing_info**](docs/SubscriptionsApi.md#set_billing_info) | **PUT** /subscriptions/{subscriptionId}/billingInfo | Billing info
*SubscriptionsApi* | [**set_custom_domain**](docs/SubscriptionsApi.md#set_custom_domain) | **PUT** /subscriptions/{subscriptionId}/custom_domain | Custom domain
*SubscriptionsApi* | [**set_default_domain**](docs/SubscriptionsApi.md#set_default_domain) | **PUT** /subscriptions/{subscriptionId}/default_domain | Default domain
*SubscriptionsApi* | [**set_domain**](docs/SubscriptionsApi.md#set_domain) | **PUT** /subscriptions/{subscriptionId}/domain | Custom domain
*SubscriptionsApi* | [**set_lock**](docs/SubscriptionsApi.md#set_lock) | **PUT** /subscriptions/{subscriptionId}/lock | Set subscription lock
*SubscriptionsApi* | [**set_note**](docs/SubscriptionsApi.md#set_note) | **PUT** /subscriptions/{subscriptionId}/note | Note
*SubscriptionsApi* | [**set_owner_email**](docs/SubscriptionsApi.md#set_owner_email) | **PUT** /subscriptions/{subscriptionId}/owner_email | Owner&#39;s email
*SubscriptionsApi* | [**set_pap_tracking_params**](docs/SubscriptionsApi.md#set_pap_tracking_params) | **PUT** /subscriptions/{subscriptionId}/pap_tracking_params | PAP tracking params
*SubscriptionsApi* | [**set_payment_method**](docs/SubscriptionsApi.md#set_payment_method) | **PUT** /subscriptions/{subscriptionId}/paymentMethod | Payment method
*SubscriptionsApi* | [**set_source**](docs/SubscriptionsApi.md#set_source) | **PUT** /subscriptions/{subscriptionId}/source | Install source
*SubscriptionsApi* | [**set_subscription_usage**](docs/SubscriptionsApi.md#set_subscription_usage) | **PUT** /subscriptions/{subscriptionId}/usage | Subscription usage
*SubscriptionsApi* | [**set_update_policy**](docs/SubscriptionsApi.md#set_update_policy) | **PUT** /subscriptions/{subscriptionId}/update_policy | Set update policy
*SubscriptionsApi* | [**signup**](docs/SubscriptionsApi.md#signup) | **POST** /subscriptions | Create subscription
*SubscriptionsApi* | [**stop_billing**](docs/SubscriptionsApi.md#stop_billing) | **POST** /subscriptions/{subscriptionId}/_stop | Stop billing
*SubscriptionsApi* | [**suspend**](docs/SubscriptionsApi.md#suspend) | **POST** /subscriptions/{subscriptionId}/_suspend | Suspend subscription
*SubscriptionsApi* | [**terminate**](docs/SubscriptionsApi.md#terminate) | **POST** /subscriptions/{subscriptionId}/_terminate | Terminate subscription
*SubscriptionsApi* | [**unsuspend**](docs/SubscriptionsApi.md#unsuspend) | **POST** /subscriptions/{subscriptionId}/_unsuspend | Unsuspend subscription
*SubscriptionsApi* | [**update_application**](docs/SubscriptionsApi.md#update_application) | **POST** /subscriptions/{subscriptionId}/_update | Update subscription
*SubscriptionsApi* | [**validate_billing_info**](docs/SubscriptionsApi.md#validate_billing_info) | **POST** /subscriptions/{subscriptionId}/_validateBillingInfo | Test Billing info
*TasksApi* | [**get_rich_task**](docs/TasksApi.md#get_rich_task) | **GET** /executor/tasks/{taskId} | Task
*TasksApi* | [**get_rich_task_attempt**](docs/TasksApi.md#get_rich_task_attempt) | **GET** /executor/task_attempts/{taskAttemptId} | Task attempt
*TasksApi* | [**get_task_action**](docs/TasksApi.md#get_task_action) | **GET** /executor/actions/{actionId} | Action
*TasksApi* | [**get_task_minion_job**](docs/TasksApi.md#get_task_minion_job) | **GET** /executor/actions/{actionId}/minion_jobs/{minionId} | Minion job
*TasksApi* | [**get_tasks**](docs/TasksApi.md#get_tasks) | **GET** /executor/tasks | List of tasks
*TasksApi* | [**mark_task_broken**](docs/TasksApi.md#mark_task_broken) | **POST** /executor/tasks/{taskId}/_mark_broken | Mark task broken
*TasksApi* | [**retry_task_attempt**](docs/TasksApi.md#retry_task_attempt) | **POST** /executor/tasks/{taskAttemptId}/_retry | Retry task attempt
*TemplatesApi* | [**get_template**](docs/TemplatesApi.md#get_template) | **GET** /templates/{templateId} | Template
*TemplatesApi* | [**get_templates**](docs/TemplatesApi.md#get_templates) | **GET** /templates | Template list
*TemplatesApi* | [**update_template**](docs/TemplatesApi.md#update_template) | **PUT** /templates/{templateId} | Template
*TokenApi* | [**get_access_token**](docs/TokenApi.md#get_access_token) | **POST** /token | Access token
*VariationsApi* | [**get_all_variation_addons**](docs/VariationsApi.md#get_all_variation_addons) | **GET** /variations/{variationId}/addons | Variations addons
*VariationsApi* | [**get_variation**](docs/VariationsApi.md#get_variation) | **GET** /variations/{variationId} | Variation
*VariationsApi* | [**get_variation_addons**](docs/VariationsApi.md#get_variation_addons) | **GET** /variations/{variationId}/available_addons | Variations addons
*VariationsApi* | [**get_variations**](docs/VariationsApi.md#get_variations) | **GET** /variations | Variation list


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountManager](docs/AccountManager.md)
 - [AccountStats](docs/AccountStats.md)
 - [AccountUser](docs/AccountUser.md)
 - [Addon](docs/Addon.md)
 - [AddonList](docs/AddonList.md)
 - [AgentsCount](docs/AgentsCount.md)
 - [AgentsStats](docs/AgentsStats.md)
 - [AsteriskHost](docs/AsteriskHost.md)
 - [Attribute](docs/Attribute.md)
 - [AttributeSimple](docs/AttributeSimple.md)
 - [AwsRegion](docs/AwsRegion.md)
 - [BilledPeriod](docs/BilledPeriod.md)
 - [BilledPeriodItem](docs/BilledPeriodItem.md)
 - [BillingInfo](docs/BillingInfo.md)
 - [BillingMetric](docs/BillingMetric.md)
 - [BillingParameters](docs/BillingParameters.md)
 - [BillingStatus](docs/BillingStatus.md)
 - [BooleanResponse](docs/BooleanResponse.md)
 - [CalculatedItem](docs/CalculatedItem.md)
 - [CalculatedItems](docs/CalculatedItems.md)
 - [Country](docs/Country.md)
 - [Coupon](docs/Coupon.md)
 - [Credentials](docs/Credentials.md)
 - [CustomDomain](docs/CustomDomain.md)
 - [Customer](docs/Customer.md)
 - [DefaultDomain](docs/DefaultDomain.md)
 - [DeletionMarker](docs/DeletionMarker.md)
 - [DevSignup](docs/DevSignup.md)
 - [Discount](docs/Discount.md)
 - [DiscountTemplate](docs/DiscountTemplate.md)
 - [DiscountValue](docs/DiscountValue.md)
 - [Domain](docs/Domain.md)
 - [Email](docs/Email.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventLogs](docs/EventLogs.md)
 - [FailedPayment](docs/FailedPayment.md)
 - [HackDummyPayment](docs/HackDummyPayment.md)
 - [HostedApiKey](docs/HostedApiKey.md)
 - [Ids](docs/Ids.md)
 - [IndexStatus](docs/IndexStatus.md)
 - [InitialLang](docs/InitialLang.md)
 - [InitialLoginAttempts](docs/InitialLoginAttempts.md)
 - [InstallProgress](docs/InstallProgress.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceItem](docs/InvoiceItem.md)
 - [KnowledgebasesCount](docs/KnowledgebasesCount.md)
 - [LaKbCollection](docs/LaKbCollection.md)
 - [LaKbDomain](docs/LaKbDomain.md)
 - [LaKbParked](docs/LaKbParked.md)
 - [LaKbProxy](docs/LaKbProxy.md)
 - [LoginUrl](docs/LoginUrl.md)
 - [MassResponse](docs/MassResponse.md)
 - [Message](docs/Message.md)
 - [Minion](docs/Minion.md)
 - [MinionInfo](docs/MinionInfo.md)
 - [MinionJob](docs/MinionJob.md)
 - [MyAccountParameters](docs/MyAccountParameters.md)
 - [MyAccountToken](docs/MyAccountToken.md)
 - [Note](docs/Note.md)
 - [OwnerEmail](docs/OwnerEmail.md)
 - [PapTrackingParams](docs/PapTrackingParams.md)
 - [PaymentErrorInfo](docs/PaymentErrorInfo.md)
 - [PaymentInfo](docs/PaymentInfo.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentProcessorType](docs/PaymentProcessorType.md)
 - [PeriodPricing](docs/PeriodPricing.md)
 - [Product](docs/Product.md)
 - [ProductVersion](docs/ProductVersion.md)
 - [PublicIp](docs/PublicIp.md)
 - [RangeValue](docs/RangeValue.md)
 - [RedeemCode](docs/RedeemCode.md)
 - [RedeemCodeSignup](docs/RedeemCodeSignup.md)
 - [RedeemCodesImport](docs/RedeemCodesImport.md)
 - [Redemption](docs/Redemption.md)
 - [Refund](docs/Refund.md)
 - [RefundRequest](docs/RefundRequest.md)
 - [ReindexData](docs/ReindexData.md)
 - [ReindexStatusData](docs/ReindexStatusData.md)
 - [ResellerSignup](docs/ResellerSignup.md)
 - [ResellerSubscription](docs/ResellerSubscription.md)
 - [ResellerUpgrade](docs/ResellerUpgrade.md)
 - [SaleStats](docs/SaleStats.md)
 - [Score](docs/Score.md)
 - [Setting](docs/Setting.md)
 - [SettingGroup](docs/SettingGroup.md)
 - [Signup](docs/Signup.md)
 - [Source](docs/Source.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionStatusHistory](docs/SubscriptionStatusHistory.md)
 - [SubscriptionViewData](docs/SubscriptionViewData.md)
 - [SubscriptionViewDb](docs/SubscriptionViewDb.md)
 - [Summary](docs/Summary.md)
 - [SummaryHistoryItem](docs/SummaryHistoryItem.md)
 - [SummaryInvoice](docs/SummaryInvoice.md)
 - [Task](docs/Task.md)
 - [TaskAttempt](docs/TaskAttempt.md)
 - [TaskStep](docs/TaskStep.md)
 - [TaskStepAction](docs/TaskStepAction.md)
 - [Template](docs/Template.md)
 - [Token](docs/Token.md)
 - [TrackGaClient](docs/TrackGaClient.md)
 - [TrackPapSignupIp](docs/TrackPapSignupIp.md)
 - [TrackPapUserAgent](docs/TrackPapUserAgent.md)
 - [Upgrade](docs/Upgrade.md)
 - [UpgradeUrl](docs/UpgradeUrl.md)
 - [UsageData](docs/UsageData.md)
 - [ValidityExtension](docs/ValidityExtension.md)
 - [Variation](docs/Variation.md)
 - [VariationUpgrade](docs/VariationUpgrade.md)
 - [VariationUpgrades](docs/VariationUpgrades.md)
 - [VersionInfo](docs/VersionInfo.md)
 - [VersionName](docs/VersionName.md)
 - [VersionStats](docs/VersionStats.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="privileges"></a>
### privileges

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: 
- **Scopes**: 
 - **hack.dummy_payment**: set dummy payment
 - **agent.login**: Log into an account
 - **attribute.read**: Read attributes
 - **attribute.write**: Change attributes
 - **dev.create_subscription**: Create dev subscription
 - **event_logs.read**: Event logs read
 - **invoice.read**: Read invoices
 - **job.read**: Jobs read
 - **product.read**: Products read
 - **product.write**: Products write
 - **refund.read**: Refunds read
 - **refund.write**: Refunds write
 - **reseller.own**: Read info related to reseller making the call
 - **reseller.signup**: Create new reseller subscription
 - **reseller.read**: Read information about reseller
 - **reseller.write**: Manage reseller or reseller subscriptions
 - **subscription.own**: Read/write own subscriptions (use 'me' as subscriptionId)
 - **subscription.read**: Subscriptions read
 - **subscription.basicOperations**: Subscriptions operations allowed for agent
 - **subscription.write**: Subscriptions write
 - **subscription.delete**: Subscriptions delete
 - **subscription.reindex**: Reindex of account
 - **subscription.massActions**: Subscriptions mass actions
 - **subscription.changeDomain**: Change default or custom domain
 - **subscription.changeDefaultDomain**: Change default domain
 - **subscription.changeCustomDomain**: Change custom domain
 - **task.read**: Tasks read
 - **task.write**: Tasks write
 - **template.read**: Read templates
 - **template.write**: Change templates
 - **variation.read**: Variations read
 - **minion.read**: Minions read
 - **minion.write**: Minions write
 - **stats.sale**: Sale stats
 - **stats.account**: Account numbers stats
 - **settings.read**: Read settings
 - **settings.write**: Change settings
 - **stats.versions**: Get stat versions
 - **stats.agents**: Get stat agents


## Author

support@qualityunit.com

