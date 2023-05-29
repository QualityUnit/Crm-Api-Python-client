# qu.crm.DevApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dev_create_subscription**](DevApi.md#dev_create_subscription) | **POST** /dev/_create_subscription | Create dev subscription


# **dev_create_subscription**
> Subscription dev_create_subscription(body=body)

Create dev subscription

Create dev subscription

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.dev_signup import DevSignup
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
    api_instance = qu.crm.DevApi(api_client)
    body = qu.crm.DevSignup() # DevSignup |  (optional)

    try:
        # Create dev subscription
        api_response = await api_instance.dev_create_subscription(body=body)
        print("The response of DevApi->dev_create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevApi->dev_create_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevSignup**](DevSignup.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

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

