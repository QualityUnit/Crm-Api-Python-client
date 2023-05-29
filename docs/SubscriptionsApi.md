# qu.crm.SubscriptionsApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_free_addons**](SubscriptionsApi.md#add_free_addons) | **POST** /subscriptions/{subscriptionId}/_addFreeAddons | Add free addons
[**aet_account_manager**](SubscriptionsApi.md#aet_account_manager) | **PUT** /subscriptions/{subscriptionId}/account_manager | Assign account manager
[**agree_with_request_billing**](SubscriptionsApi.md#agree_with_request_billing) | **POST** /subscriptions/{subscriptionId}/pap_request_billing | PAP agree with additional billing
[**change_addons**](SubscriptionsApi.md#change_addons) | **PUT** /subscriptions/{subscriptionId}/addons | Addon change
[**change_plan**](SubscriptionsApi.md#change_plan) | **POST** /subscriptions/{subscriptionId}/_upgrade | Change plan
[**check_domain**](SubscriptionsApi.md#check_domain) | **POST** /subscriptions/_check_domain | Domain availability
[**clear_last_payment_fail**](SubscriptionsApi.md#clear_last_payment_fail) | **POST** /subscriptions/{subscriptionId}/_clearLastPaymentFail | Clear last payment fail
[**delete**](SubscriptionsApi.md#delete) | **POST** /subscriptions/{subscriptionId}/_delete | Delete subscription
[**extend_validity**](SubscriptionsApi.md#extend_validity) | **POST** /subscriptions/{subscriptionId}/_extendValidity | Extends account validity
[**get_account**](SubscriptionsApi.md#get_account) | **GET** /accounts/{accountId} | Account
[**get_account_manager**](SubscriptionsApi.md#get_account_manager) | **GET** /subscriptions/{subscriptionId}/account_manager | Get account manager
[**get_active_addons**](SubscriptionsApi.md#get_active_addons) | **GET** /subscriptions/{subscriptionId}/addons | Addon list
[**get_billing_info**](SubscriptionsApi.md#get_billing_info) | **GET** /subscriptions/{subscriptionId}/billingInfo | Billing info
[**get_billing_metrics**](SubscriptionsApi.md#get_billing_metrics) | **GET** /subscriptions/{subscriptionId}/billingMetrics | Billing metrics
[**get_billing_status**](SubscriptionsApi.md#get_billing_status) | **GET** /subscriptions/{subscriptionId}/billingStatus | Billing status
[**get_domain_info**](SubscriptionsApi.md#get_domain_info) | **GET** /subscriptions/{subscriptionId}/domain | Domain info
[**get_failed_payment**](SubscriptionsApi.md#get_failed_payment) | **GET** /failed_payments/{failedPaymentId} | Failed payment
[**get_failed_payments**](SubscriptionsApi.md#get_failed_payments) | **GET** /failed_payments | Failed payment list
[**get_install_progress**](SubscriptionsApi.md#get_install_progress) | **GET** /subscriptions/{subscriptionId}/install_progress | Install progress
[**get_note**](SubscriptionsApi.md#get_note) | **GET** /subscriptions/{subscriptionId}/note | Note
[**get_payment_method**](SubscriptionsApi.md#get_payment_method) | **GET** /subscriptions/{subscriptionId}/paymentMethod | Payment method
[**get_payment_processor**](SubscriptionsApi.md#get_payment_processor) | **GET** /subscriptions/{subscriptionId}/paymentProcessor | Payment processor
[**get_source**](SubscriptionsApi.md#get_source) | **GET** /subscriptions/{subscriptionId}/source | Install source
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription
[**get_subscription_attributes**](SubscriptionsApi.md#get_subscription_attributes) | **GET** /subscriptions/{subscriptionId}/attributes | Subscription attribute list
[**get_subscription_discounts**](SubscriptionsApi.md#get_subscription_discounts) | **GET** /subscriptions/{subscriptionId}/discounts | Subscription discounts
[**get_subscription_invoices**](SubscriptionsApi.md#get_subscription_invoices) | **GET** /subscriptions/{subscriptionId}/invoices | Subscription invoice list
[**get_subscriptions**](SubscriptionsApi.md#get_subscriptions) | **GET** /subscriptions | Subscription list
[**get_upgrade_variations**](SubscriptionsApi.md#get_upgrade_variations) | **GET** /subscriptions/{subscriptionId}/upgradeVariations | Upgrade variation list
[**is_additional_billing_agreed**](SubscriptionsApi.md#is_additional_billing_agreed) | **GET** /subscriptions/{subscriptionId}/pap_request_billing | PAP get additional billing
[**refresh_account**](SubscriptionsApi.md#refresh_account) | **POST** /subscriptions/{subscriptionId}/_refreshAccount | Refresh account
[**remove_lock**](SubscriptionsApi.md#remove_lock) | **PUT** /subscriptions/{subscriptionId}/unlock | Remove lock
[**resume_billing**](SubscriptionsApi.md#resume_billing) | **POST** /subscriptions/{subscriptionId}/_cancelStop | Restart billing
[**set_billing_info**](SubscriptionsApi.md#set_billing_info) | **PUT** /subscriptions/{subscriptionId}/billingInfo | Billing info
[**set_custom_domain**](SubscriptionsApi.md#set_custom_domain) | **PUT** /subscriptions/{subscriptionId}/custom_domain | Custom domain
[**set_default_domain**](SubscriptionsApi.md#set_default_domain) | **PUT** /subscriptions/{subscriptionId}/default_domain | Default domain
[**set_domain**](SubscriptionsApi.md#set_domain) | **PUT** /subscriptions/{subscriptionId}/domain | Custom domain
[**set_lock**](SubscriptionsApi.md#set_lock) | **PUT** /subscriptions/{subscriptionId}/lock | Set subscription lock
[**set_note**](SubscriptionsApi.md#set_note) | **PUT** /subscriptions/{subscriptionId}/note | Note
[**set_owner_email**](SubscriptionsApi.md#set_owner_email) | **PUT** /subscriptions/{subscriptionId}/owner_email | Owner&#39;s email
[**set_pap_tracking_params**](SubscriptionsApi.md#set_pap_tracking_params) | **PUT** /subscriptions/{subscriptionId}/pap_tracking_params | PAP tracking params
[**set_payment_method**](SubscriptionsApi.md#set_payment_method) | **PUT** /subscriptions/{subscriptionId}/paymentMethod | Payment method
[**set_source**](SubscriptionsApi.md#set_source) | **PUT** /subscriptions/{subscriptionId}/source | Install source
[**set_subscription_usage**](SubscriptionsApi.md#set_subscription_usage) | **PUT** /subscriptions/{subscriptionId}/usage | Subscription usage
[**set_update_policy**](SubscriptionsApi.md#set_update_policy) | **PUT** /subscriptions/{subscriptionId}/update_policy | Set update policy
[**signup**](SubscriptionsApi.md#signup) | **POST** /subscriptions | Create subscription
[**stop_billing**](SubscriptionsApi.md#stop_billing) | **POST** /subscriptions/{subscriptionId}/_stop | Stop billing
[**suspend**](SubscriptionsApi.md#suspend) | **POST** /subscriptions/{subscriptionId}/_suspend | Suspend subscription
[**terminate**](SubscriptionsApi.md#terminate) | **POST** /subscriptions/{subscriptionId}/_terminate | Terminate subscription
[**unsuspend**](SubscriptionsApi.md#unsuspend) | **POST** /subscriptions/{subscriptionId}/_unsuspend | Unsuspend subscription
[**update_application**](SubscriptionsApi.md#update_application) | **POST** /subscriptions/{subscriptionId}/_update | Update subscription
[**validate_billing_info**](SubscriptionsApi.md#validate_billing_info) | **POST** /subscriptions/{subscriptionId}/_validateBillingInfo | Test Billing info


# **add_free_addons**
> object add_free_addons(subscription_id, body=body)

Add free addons

Makes specified addons active and free until they are deactivated or plan is changed.

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.addon_list import AddonList
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.AddonList() # AddonList |  (optional)

    try:
        # Add free addons
        api_response = await api_instance.add_free_addons(subscription_id, body=body)
        print("The response of SubscriptionsApi->add_free_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->add_free_addons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**AddonList**](AddonList.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aet_account_manager**
> object aet_account_manager(subscription_id, body=body)

Assign account manager

Assign agent to manage this subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.account_manager import AccountManager
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.AccountManager() # AccountManager |  (optional)

    try:
        # Assign account manager
        api_response = await api_instance.aet_account_manager(subscription_id, body=body)
        print("The response of SubscriptionsApi->aet_account_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->aet_account_manager: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**AccountManager**](AccountManager.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agree_with_request_billing**
> object agree_with_request_billing(subscription_id)

PAP agree with additional billing

Agree with additional billing

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # PAP agree with additional billing
        api_response = await api_instance.agree_with_request_billing(subscription_id)
        print("The response of SubscriptionsApi->agree_with_request_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->agree_with_request_billing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_addons**
> List[Addon] change_addons(subscription_id, body=body)

Addon change

Change active subscription addons

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.addon import Addon
from qu.crm.models.addon_list import AddonList
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.AddonList() # AddonList |  (optional)

    try:
        # Addon change
        api_response = await api_instance.change_addons(subscription_id, body=body)
        print("The response of SubscriptionsApi->change_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->change_addons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**AddonList**](AddonList.md)|  | [optional] 

### Return type

[**List[Addon]**](Addon.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New subscription addons list (without price field) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_plan**
> object change_plan(subscription_id, body=body)

Change plan

Upgrade subscription to another variation. In case of upgrade from paid to paid, it's possible to change country without changing payment method. If change is between EU and not EU, different payment rules might apply.

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.upgrade import Upgrade
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.Upgrade() # Upgrade |  (optional)

    try:
        # Change plan
        api_response = await api_instance.change_plan(subscription_id, body=body)
        print("The response of SubscriptionsApi->change_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->change_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**Upgrade**](Upgrade.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**201** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_domain**
> object check_domain(product_id, subdomain)

Domain availability

Check domain availability

### Example

```python
import time
import os
import qu.crm
from qu.crm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://crm.qualityunit.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = qu.crm.Configuration(
    host = "https://crm.qualityunit.com/api/v3"
)


# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.SubscriptionsApi(api_client)
    product_id = 'product_id_example' # str | 
    subdomain = 'subdomain_example' # str | 

    try:
        # Domain availability
        api_response = await api_instance.check_domain(product_id, subdomain)
        print("The response of SubscriptionsApi->check_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->check_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **subdomain** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_last_payment_fail**
> object clear_last_payment_fail(subscription_id)

Clear last payment fail

Clear last payment fail, causing automatic retry

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Clear last payment fail
        api_response = await api_instance.clear_last_payment_fail(subscription_id)
        print("The response of SubscriptionsApi->clear_last_payment_fail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->clear_last_payment_fail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(subscription_id)

Delete subscription

Delete subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Delete subscription
        api_response = await api_instance.delete(subscription_id)
        print("The response of SubscriptionsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_validity**
> object extend_validity(subscription_id, valid_to)

Extends account validity

Extends account validity

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    valid_to = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Extends account validity
        api_response = await api_instance.extend_validity(subscription_id, valid_to)
        print("The response of SubscriptionsApi->extend_validity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->extend_validity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **valid_to** | **datetime**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(account_id)

Account

Returns account

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.account import Account
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Account
        api_response = await api_instance.get_account(account_id)
        print("The response of SubscriptionsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_manager**
> AccountManager get_account_manager(subscription_id)

Get account manager

Returns agent assigned to manage this subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.account_manager import AccountManager
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get account manager
        api_response = await api_instance.get_account_manager(subscription_id)
        print("The response of SubscriptionsApi->get_account_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_account_manager: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**AccountManager**](AccountManager.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account manager |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_addons**
> List[Addon] get_active_addons(subscription_id)

Addon list

Returns list of active subscription addons

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.addon import Addon
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Addon list
        api_response = await api_instance.get_active_addons(subscription_id)
        print("The response of SubscriptionsApi->get_active_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_active_addons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[Addon]**](Addon.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription addon list (without price field) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_info**
> Customer get_billing_info(subscription_id)

Billing info

Returns billing info

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.customer import Customer
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Billing info
        api_response = await api_instance.get_billing_info(subscription_id)
        print("The response of SubscriptionsApi->get_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_billing_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_metrics**
> List[BillingMetric] get_billing_metrics(subscription_id)

Billing metrics

Returns billing metrics

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.billing_metric import BillingMetric
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Billing metrics
        api_response = await api_instance.get_billing_metrics(subscription_id)
        print("The response of SubscriptionsApi->get_billing_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_billing_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[BillingMetric]**](BillingMetric.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing metrics |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_status**
> BillingStatus get_billing_status(subscription_id)

Billing status

Returns billing status

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.billing_status import BillingStatus
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Billing status
        api_response = await api_instance.get_billing_status(subscription_id)
        print("The response of SubscriptionsApi->get_billing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_billing_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**BillingStatus**](BillingStatus.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_info**
> Domain get_domain_info(subscription_id)

Domain info

Returns domain info

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.domain import Domain
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Domain info
        api_response = await api_instance.get_domain_info(subscription_id)
        print("The response of SubscriptionsApi->get_domain_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_domain_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_failed_payment**
> FailedPayment get_failed_payment(failed_payment_id)

Failed payment

Returns failed payment

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.failed_payment import FailedPayment
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    failed_payment_id = 56 # int | 

    try:
        # Failed payment
        api_response = await api_instance.get_failed_payment(failed_payment_id)
        print("The response of SubscriptionsApi->get_failed_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_failed_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **failed_payment_id** | **int**|  | 

### Return type

[**FailedPayment**](FailedPayment.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Failed payment |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_failed_payments**
> List[FailedPayment] get_failed_payments(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Failed payment list

Returns list of all failed charges

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.failed_payment import FailedPayment
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Failed payment list
        api_response = await api_instance.get_failed_payments(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of SubscriptionsApi->get_failed_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_failed_payments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Used only if _from is not defined. | [optional] 
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] 
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 
 **var_from** | **int**| Result set start. Takes precedence over _page if defined. | [optional] 
 **to** | **int**| Result set end. Used only if _from is used. | [optional] 

### Return type

[**List[FailedPayment]**](FailedPayment.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Failed payments |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_install_progress**
> InstallProgress get_install_progress(subscription_id)

Install progress

Returns subscription installation progress

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.install_progress import InstallProgress
from qu.crm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://crm.qualityunit.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = qu.crm.Configuration(
    host = "https://crm.qualityunit.com/api/v3"
)


# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Install progress
        api_response = await api_instance.get_install_progress(subscription_id)
        print("The response of SubscriptionsApi->get_install_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_install_progress: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**InstallProgress**](InstallProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installation progress response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note**
> Note get_note(subscription_id)

Note

Returns subscription note

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.note import Note
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Note
        api_response = await api_instance.get_note(subscription_id)
        print("The response of SubscriptionsApi->get_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_note: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Note**](Note.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription note |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> PaymentInfo get_payment_method(subscription_id)

Payment method

Returns payment method

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.payment_info import PaymentInfo
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Payment method
        api_response = await api_instance.get_payment_method(subscription_id)
        print("The response of SubscriptionsApi->get_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**PaymentInfo**](PaymentInfo.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment method info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_processor**
> PaymentProcessorType get_payment_processor(subscription_id, payment_type, country=country)

Payment processor

Returns payment processor to use when updating payment method

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.payment_processor_type import PaymentProcessorType
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    payment_type = 'payment_type_example' # str | 
    country = 'country_example' # str |  (optional)

    try:
        # Payment processor
        api_response = await api_instance.get_payment_processor(subscription_id, payment_type, country=country)
        print("The response of SubscriptionsApi->get_payment_processor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_payment_processor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **payment_type** | **str**|  | 
 **country** | **str**|  | [optional] 

### Return type

[**PaymentProcessorType**](PaymentProcessorType.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment processor type |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source**
> Source get_source(subscription_id)

Install source

Returns source of subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.source import Source
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Install source
        api_response = await api_instance.get_source(subscription_id)
        print("The response of SubscriptionsApi->get_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Source**](Source.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription note |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> Subscription get_subscription(subscription_id)

Subscription

Returns subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.subscription import Subscription
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Subscription
        api_response = await api_instance.get_subscription(subscription_id)
        print("The response of SubscriptionsApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_attributes**
> List[AttributeSimple] get_subscription_attributes(subscription_id)

Subscription attribute list

Returns list of subscription attributes

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.attribute_simple import AttributeSimple
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Subscription attribute list
        api_response = await api_instance.get_subscription_attributes(subscription_id)
        print("The response of SubscriptionsApi->get_subscription_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_attributes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[AttributeSimple]**](AttributeSimple.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoices response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_discounts**
> List[DiscountValue] get_subscription_discounts(subscription_id)

Subscription discounts

Returns all active discounts for specified subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.discount_value import DiscountValue
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Subscription discounts
        api_response = await api_instance.get_subscription_discounts(subscription_id)
        print("The response of SubscriptionsApi->get_subscription_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_discounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[DiscountValue]**](DiscountValue.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discounts |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_invoices**
> List[Invoice] get_subscription_invoices(subscription_id, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Subscription invoice list

Returns list of subscription invoices

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.invoice import Invoice
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Subscription invoice list
        api_response = await api_instance.get_subscription_invoices(subscription_id, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of SubscriptionsApi->get_subscription_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **page** | **int**| Page to display. Used only if _from is not defined. | [optional] 
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] 
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 
 **var_from** | **int**| Result set start. Takes precedence over _page if defined. | [optional] 
 **to** | **int**| Result set end. Used only if _from is used. | [optional] 

### Return type

[**List[Invoice]**](Invoice.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoices response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> List[Subscription] get_subscriptions(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Subscription list

Returns list of subscriptions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.subscription import Subscription
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Subscription list
        api_response = await api_instance.get_subscriptions(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of SubscriptionsApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Used only if _from is not defined. | [optional] 
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] 
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 
 **var_from** | **int**| Result set start. Takes precedence over _page if defined. | [optional] 
 **to** | **int**| Result set end. Used only if _from is used. | [optional] 

### Return type

[**List[Subscription]**](Subscription.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_variations**
> VariationUpgrades get_upgrade_variations(subscription_id, country=country, vat_id=vat_id)

Upgrade variation list

Returns list of variations user can upgrade to and their current variation.

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.variation_upgrades import VariationUpgrades
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    country = 'country_example' # str |  (optional)
    vat_id = 'vat_id_example' # str |  (optional)

    try:
        # Upgrade variation list
        api_response = await api_instance.get_upgrade_variations(subscription_id, country=country, vat_id=vat_id)
        print("The response of SubscriptionsApi->get_upgrade_variations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_upgrade_variations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **country** | **str**|  | [optional] 
 **vat_id** | **str**|  | [optional] 

### Return type

[**VariationUpgrades**](VariationUpgrades.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available upgrades response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_additional_billing_agreed**
> BooleanResponse is_additional_billing_agreed(subscription_id)

PAP get additional billing

Returns agreement of additional billing

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.boolean_response import BooleanResponse
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # PAP get additional billing
        api_response = await api_instance.is_additional_billing_agreed(subscription_id)
        print("The response of SubscriptionsApi->is_additional_billing_agreed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->is_additional_billing_agreed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agreement value |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_account**
> object refresh_account(subscription_id)

Refresh account

Refresh account

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Refresh account
        api_response = await api_instance.refresh_account(subscription_id)
        print("The response of SubscriptionsApi->refresh_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->refresh_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_lock**
> object remove_lock(subscription_id, lock)

Remove lock

Remove subscription lock

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    lock = 'lock_example' # str | 

    try:
        # Remove lock
        api_response = await api_instance.remove_lock(subscription_id, lock)
        print("The response of SubscriptionsApi->remove_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->remove_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **lock** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_billing**
> object resume_billing(subscription_id, reason=reason)

Restart billing

If account billing is stopped, restart it.

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.message import Message
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    reason = qu.crm.Message() # Message | Reason for restarting (optional)

    try:
        # Restart billing
        api_response = await api_instance.resume_billing(subscription_id, reason=reason)
        print("The response of SubscriptionsApi->resume_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->resume_billing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **reason** | [**Message**](Message.md)| Reason for restarting | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_billing_info**
> object set_billing_info(subscription_id, body=body)

Billing info

Upgrade billing info

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.billing_info import BillingInfo
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.BillingInfo() # BillingInfo |  (optional)

    try:
        # Billing info
        api_response = await api_instance.set_billing_info(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_billing_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**BillingInfo**](BillingInfo.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_custom_domain**
> object set_custom_domain(subscription_id, body=body)

Custom domain

Set custom domain for account

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.custom_domain import CustomDomain
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.CustomDomain() # CustomDomain | Custom domain can be set only with both key and certificate present, or empty domain to reset. (optional)

    try:
        # Custom domain
        api_response = await api_instance.set_custom_domain(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_custom_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_custom_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**CustomDomain**](CustomDomain.md)| Custom domain can be set only with both key and certificate present, or empty domain to reset. | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_domain**
> object set_default_domain(subscription_id, body=body)

Default domain

Set default domain for account

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.default_domain import DefaultDomain
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.DefaultDomain() # DefaultDomain | Default domain can be set any time. (optional)

    try:
        # Default domain
        api_response = await api_instance.set_default_domain(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_default_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_default_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**DefaultDomain**](DefaultDomain.md)| Default domain can be set any time. | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_domain**
> object set_domain(subscription_id, body=body)

Custom domain

Park custom domain on an account

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.domain import Domain
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.Domain() # Domain | Domain can be sent anytime. Custom domain can be sent by itself or along with both certificate and key. (optional)

    try:
        # Custom domain
        api_response = await api_instance.set_domain(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**Domain**](Domain.md)| Domain can be sent anytime. Custom domain can be sent by itself or along with both certificate and key. | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_lock**
> object set_lock(subscription_id, lock)

Set subscription lock

Set subscription lock

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    lock = 'lock_example' # str | 

    try:
        # Set subscription lock
        api_response = await api_instance.set_lock(subscription_id, lock)
        print("The response of SubscriptionsApi->set_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **lock** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_note**
> object set_note(subscription_id, body=body)

Note

Set subscription note

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.note import Note
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.Note() # Note |  (optional)

    try:
        # Note
        api_response = await api_instance.set_note(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_note: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**Note**](Note.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_owner_email**
> object set_owner_email(subscription_id, body=body)

Owner's email

Set subscription owner's email

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.owner_email import OwnerEmail
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.OwnerEmail() # OwnerEmail |  (optional)

    try:
        # Owner's email
        api_response = await api_instance.set_owner_email(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_owner_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_owner_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**OwnerEmail**](OwnerEmail.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pap_tracking_params**
> object set_pap_tracking_params(subscription_id, body=body)

PAP tracking params

Set PAP tracking params

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.pap_tracking_params import PapTrackingParams
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.PapTrackingParams() # PapTrackingParams |  (optional)

    try:
        # PAP tracking params
        api_response = await api_instance.set_pap_tracking_params(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_pap_tracking_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_pap_tracking_params: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**PapTrackingParams**](PapTrackingParams.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_payment_method**
> PaymentInfo set_payment_method(subscription_id, body=body)

Payment method

Upgrade payment method

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.payment_info import PaymentInfo
from qu.crm.models.payment_method import PaymentMethod
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.PaymentMethod() # PaymentMethod |  (optional)

    try:
        # Payment method
        api_response = await api_instance.set_payment_method(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**PaymentMethod**](PaymentMethod.md)|  | [optional] 

### Return type

[**PaymentInfo**](PaymentInfo.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New payment method info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_source**
> object set_source(subscription_id, body=body)

Install source

Set source of subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.source import Source
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.Source() # Source |  (optional)

    try:
        # Install source
        api_response = await api_instance.set_source(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**Source**](Source.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_subscription_usage**
> object set_subscription_usage(subscription_id, body=body)

Subscription usage

Returns subscription usage

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.usage_data import UsageData
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.UsageData() # UsageData |  (optional)

    try:
        # Subscription usage
        api_response = await api_instance.set_subscription_usage(subscription_id, body=body)
        print("The response of SubscriptionsApi->set_subscription_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_subscription_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**UsageData**](UsageData.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_update_policy**
> object set_update_policy(subscription_id, policy)

Set update policy

Set update policy

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    policy = 'policy_example' # str | 

    try:
        # Set update policy
        api_response = await api_instance.set_update_policy(subscription_id, policy)
        print("The response of SubscriptionsApi->set_update_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->set_update_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **policy** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup**
> Subscription signup(body=body)

Create subscription

Create subscription

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.signup import Signup
from qu.crm.models.subscription import Subscription
from qu.crm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://crm.qualityunit.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = qu.crm.Configuration(
    host = "https://crm.qualityunit.com/api/v3"
)


# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.SubscriptionsApi(api_client)
    body = qu.crm.Signup() # Signup |  (optional)

    try:
        # Create subscription
        api_response = await api_instance.signup(body=body)
        print("The response of SubscriptionsApi->signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Signup**](Signup.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_billing**
> object stop_billing(subscription_id, reason=reason)

Stop billing

Stop account. Account won't be billed anymore and will continue to work till next billing date.

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.message import Message
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    reason = qu.crm.Message() # Message | Reason for stopping (optional)

    try:
        # Stop billing
        api_response = await api_instance.stop_billing(subscription_id, reason=reason)
        print("The response of SubscriptionsApi->stop_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->stop_billing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **reason** | [**Message**](Message.md)| Reason for stopping | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend**
> object suspend(subscription_id)

Suspend subscription

Suspend subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Suspend subscription
        api_response = await api_instance.suspend(subscription_id)
        print("The response of SubscriptionsApi->suspend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->suspend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate**
> object terminate(subscription_id)

Terminate subscription

Terminate subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Terminate subscription
        api_response = await api_instance.terminate(subscription_id)
        print("The response of SubscriptionsApi->terminate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->terminate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsuspend**
> object unsuspend(subscription_id, reason, valid_days=valid_days, update_version=update_version)

Unsuspend subscription

Unsuspend subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    reason = 'reason_example' # str | Reason to unsuspend subscription
    valid_days = 7 # int | Number of days to keep account valid after unsuspend (optional) (default to 7)
    update_version = 'update_version_example' # str | Target version to which account will be updated after unsuspend (optional)

    try:
        # Unsuspend subscription
        api_response = await api_instance.unsuspend(subscription_id, reason, valid_days=valid_days, update_version=update_version)
        print("The response of SubscriptionsApi->unsuspend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->unsuspend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **reason** | **str**| Reason to unsuspend subscription | 
 **valid_days** | **int**| Number of days to keep account valid after unsuspend | [optional] [default to 7]
 **update_version** | **str**| Target version to which account will be updated after unsuspend | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> object update_application(subscription_id, version=version, confirm=confirm)

Update subscription

Update subscription to latest version

### Example

* OAuth Authentication (privileges):
```python
import time
import os
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    version = 'version_example' # str |  (optional)
    confirm = True # bool |  (optional)

    try:
        # Update subscription
        api_response = await api_instance.update_application(subscription_id, version=version, confirm=confirm)
        print("The response of SubscriptionsApi->update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->update_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **version** | **str**|  | [optional] 
 **confirm** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_billing_info**
> object validate_billing_info(subscription_id, body=body)

Test Billing info

Checks if billing info can be updated without issues. Field 'force' in BillingInfo is ignored in this call.

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.billing_info import BillingInfo
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
    api_instance = qu.crm.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.BillingInfo() # BillingInfo |  (optional)

    try:
        # Test Billing info
        api_response = await api_instance.validate_billing_info(subscription_id, body=body)
        print("The response of SubscriptionsApi->validate_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->validate_billing_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**BillingInfo**](BillingInfo.md)|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**403** | When provided billing info is valid, but updating would cause payment method to be removed because of deprecation. |  -  |
**404** | When some parts of provided billing info are missing or invalid. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

