# qu.crm.AdminPanelApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription_sources**](AdminPanelApi.md#get_subscription_sources) | **GET** /admin_panel/sources | Subscription source list
[**get_subscription_view**](AdminPanelApi.md#get_subscription_view) | **GET** /admin_panel/subscription_view/{subscriptionId} | Subscription view data


# **get_subscription_sources**
> List[Source] get_subscription_sources()

Subscription source list

Returns list of all existing subscription installation sources

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
    api_instance = qu.crm.AdminPanelApi(api_client)

    try:
        # Subscription source list
        api_response = await api_instance.get_subscription_sources()
        print("The response of AdminPanelApi->get_subscription_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminPanelApi->get_subscription_sources: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Source]**](Source.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription sources response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_view**
> SubscriptionViewData get_subscription_view(subscription_id)

Subscription view data

Returns subscription view data

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.subscription_view_data import SubscriptionViewData
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
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Subscription view data
        api_response = await api_instance.get_subscription_view(subscription_id)
        print("The response of AdminPanelApi->get_subscription_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminPanelApi->get_subscription_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**SubscriptionViewData**](SubscriptionViewData.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription view response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

