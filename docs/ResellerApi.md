# qu.crm.ResellerApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reseller_billed_periods**](ResellerApi.md#get_reseller_billed_periods) | **GET** /reseller/subscriptions/{subscriptionId}/billed_periods | Reseller subscription billed period list
[**get_reseller_invoices**](ResellerApi.md#get_reseller_invoices) | **GET** /reseller/invoices | Reseller invoice list
[**get_reseller_subscription**](ResellerApi.md#get_reseller_subscription) | **GET** /reseller/subscriptions/{subscriptionId} | Get reseller subscription
[**get_reseller_subscription_usage**](ResellerApi.md#get_reseller_subscription_usage) | **GET** /reseller/subscriptions/{subscriptionId}/usage/agents | Get reseller subscription usage
[**get_reseller_subscriptions**](ResellerApi.md#get_reseller_subscriptions) | **GET** /reseller/subscriptions | Get reseller subscriptions
[**reseller_change_plan**](ResellerApi.md#reseller_change_plan) | **POST** /reseller/subscriptions/{subscriptionId}/_upgrade | Change plan
[**reseller_signup**](ResellerApi.md#reseller_signup) | **POST** /reseller/subscriptions | Create reseller subscription
[**suspend_reseller_subscription**](ResellerApi.md#suspend_reseller_subscription) | **POST** /reseller/subscriptions/{subscriptionId}/_suspend | Suspend reseller subscription
[**unsuspend_reseller_subscription**](ResellerApi.md#unsuspend_reseller_subscription) | **POST** /reseller/subscriptions/{subscriptionId}/_unsuspend | Unsuspend reseller subscription


# **get_reseller_billed_periods**
> List[BilledPeriod] get_reseller_billed_periods(subscription_id)

Reseller subscription billed period list

Returns all billed periods of reseller subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.billed_period import BilledPeriod
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
    api_instance = qu.crm.ResellerApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Reseller subscription billed period list
        api_response = await api_instance.get_reseller_billed_periods(subscription_id)
        print("The response of ResellerApi->get_reseller_billed_periods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->get_reseller_billed_periods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[BilledPeriod]**](BilledPeriod.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billed periods response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reseller_invoices**
> List[Invoice] get_reseller_invoices()

Reseller invoice list

Returns all reseller invoices

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
    api_instance = qu.crm.ResellerApi(api_client)

    try:
        # Reseller invoice list
        api_response = await api_instance.get_reseller_invoices()
        print("The response of ResellerApi->get_reseller_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->get_reseller_invoices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_reseller_subscription**
> ResellerSubscription get_reseller_subscription(subscription_id)

Get reseller subscription

Returns subscription that belongs to the reseller

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.reseller_subscription import ResellerSubscription
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
    api_instance = qu.crm.ResellerApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get reseller subscription
        api_response = await api_instance.get_reseller_subscription(subscription_id)
        print("The response of ResellerApi->get_reseller_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->get_reseller_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**ResellerSubscription**](ResellerSubscription.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reseller subscription response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reseller_subscription_usage**
> List[RangeValue] get_reseller_subscription_usage(subscription_id, var_from, to=to)

Get reseller subscription usage

Returns usage of reseller subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.range_value import RangeValue
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
    api_instance = qu.crm.ResellerApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    var_from = '2013-10-20' # date | Start date in form 'YYYY-MM-DD' (inclusive)
    to = '2013-10-20' # date | Start date in form 'YYYY-MM-DD' (inclusive) (optional)

    try:
        # Get reseller subscription usage
        api_response = await api_instance.get_reseller_subscription_usage(subscription_id, var_from, to=to)
        print("The response of ResellerApi->get_reseller_subscription_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->get_reseller_subscription_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **var_from** | **date**| Start date in form &#39;YYYY-MM-DD&#39; (inclusive) | 
 **to** | **date**| Start date in form &#39;YYYY-MM-DD&#39; (inclusive) | [optional] 

### Return type

[**List[RangeValue]**](RangeValue.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reseller_subscriptions**
> List[ResellerSubscription] get_reseller_subscriptions()

Get reseller subscriptions

Returns all subscriptions that belong to the reseller

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.reseller_subscription import ResellerSubscription
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
    api_instance = qu.crm.ResellerApi(api_client)

    try:
        # Get reseller subscriptions
        api_response = await api_instance.get_reseller_subscriptions()
        print("The response of ResellerApi->get_reseller_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->get_reseller_subscriptions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ResellerSubscription]**](ResellerSubscription.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reseller subscriptions response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reseller_change_plan**
> object reseller_change_plan(subscription_id, reseller_upgrade)

Change plan

Move subscription to another variation.

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.reseller_upgrade import ResellerUpgrade
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
    api_instance = qu.crm.ResellerApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    reseller_upgrade = qu.crm.ResellerUpgrade() # ResellerUpgrade | 

    try:
        # Change plan
        api_response = await api_instance.reseller_change_plan(subscription_id, reseller_upgrade)
        print("The response of ResellerApi->reseller_change_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->reseller_change_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **reseller_upgrade** | [**ResellerUpgrade**](ResellerUpgrade.md)|  | 

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

# **reseller_signup**
> ResellerSubscription reseller_signup(reseller_signup)

Create reseller subscription

Create reseller subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.reseller_signup import ResellerSignup
from qu.crm.models.reseller_subscription import ResellerSubscription
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
    api_instance = qu.crm.ResellerApi(api_client)
    reseller_signup = qu.crm.ResellerSignup() # ResellerSignup | 

    try:
        # Create reseller subscription
        api_response = await api_instance.reseller_signup(reseller_signup)
        print("The response of ResellerApi->reseller_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->reseller_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reseller_signup** | [**ResellerSignup**](ResellerSignup.md)|  | 

### Return type

[**ResellerSubscription**](ResellerSubscription.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_reseller_subscription**
> object suspend_reseller_subscription(subscription_id)

Suspend reseller subscription

Suspend reseller subscription

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
    api_instance = qu.crm.ResellerApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Suspend reseller subscription
        api_response = await api_instance.suspend_reseller_subscription(subscription_id)
        print("The response of ResellerApi->suspend_reseller_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->suspend_reseller_subscription: %s\n" % e)
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

# **unsuspend_reseller_subscription**
> object unsuspend_reseller_subscription(subscription_id)

Unsuspend reseller subscription

Unsuspend reseller subscription

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
    api_instance = qu.crm.ResellerApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Unsuspend reseller subscription
        api_response = await api_instance.unsuspend_reseller_subscription(subscription_id)
        print("The response of ResellerApi->unsuspend_reseller_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResellerApi->unsuspend_reseller_subscription: %s\n" % e)
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

