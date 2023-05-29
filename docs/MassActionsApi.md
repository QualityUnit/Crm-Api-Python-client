# qu.crm.MassActionsApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mass_delete**](MassActionsApi.md#mass_delete) | **POST** /subscriptions/massAction/_delete | Delete multiple subscriptions
[**mass_suspend**](MassActionsApi.md#mass_suspend) | **POST** /subscriptions/massAction/_suspend | Suspend multiple subscriptions
[**mass_terminate**](MassActionsApi.md#mass_terminate) | **POST** /subscriptions/massAction/_terminate | Terminate multiple subscriptions
[**mass_update**](MassActionsApi.md#mass_update) | **POST** /subscriptions/massAction/_update | Update multiple subscriptions


# **mass_delete**
> MassResponse mass_delete(ids)

Delete multiple subscriptions

Delete multiple subscriptions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.ids import Ids
from qu.crm.models.mass_response import MassResponse
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
    api_instance = qu.crm.MassActionsApi(api_client)
    ids = qu.crm.Ids() # Ids | 

    try:
        # Delete multiple subscriptions
        api_response = await api_instance.mass_delete(ids)
        print("The response of MassActionsApi->mass_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MassActionsApi->mass_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**Ids**](Ids.md)|  | 

### Return type

[**MassResponse**](MassResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mass response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_suspend**
> MassResponse mass_suspend(ids)

Suspend multiple subscriptions

Suspend multiple subscriptions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.ids import Ids
from qu.crm.models.mass_response import MassResponse
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
    api_instance = qu.crm.MassActionsApi(api_client)
    ids = qu.crm.Ids() # Ids | 

    try:
        # Suspend multiple subscriptions
        api_response = await api_instance.mass_suspend(ids)
        print("The response of MassActionsApi->mass_suspend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MassActionsApi->mass_suspend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**Ids**](Ids.md)|  | 

### Return type

[**MassResponse**](MassResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mass response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_terminate**
> MassResponse mass_terminate(ids)

Terminate multiple subscriptions

Terminate multiple subscriptions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.ids import Ids
from qu.crm.models.mass_response import MassResponse
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
    api_instance = qu.crm.MassActionsApi(api_client)
    ids = qu.crm.Ids() # Ids | 

    try:
        # Terminate multiple subscriptions
        api_response = await api_instance.mass_terminate(ids)
        print("The response of MassActionsApi->mass_terminate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MassActionsApi->mass_terminate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**Ids**](Ids.md)|  | 

### Return type

[**MassResponse**](MassResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mass response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_update**
> MassResponse mass_update(ids, version=version, confirm=confirm)

Update multiple subscriptions

Update multiple subscriptions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.ids import Ids
from qu.crm.models.mass_response import MassResponse
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
    api_instance = qu.crm.MassActionsApi(api_client)
    ids = qu.crm.Ids() # Ids | 
    version = 'version_example' # str |  (optional)
    confirm = True # bool |  (optional)

    try:
        # Update multiple subscriptions
        api_response = await api_instance.mass_update(ids, version=version, confirm=confirm)
        print("The response of MassActionsApi->mass_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MassActionsApi->mass_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**Ids**](Ids.md)|  | 
 **version** | **str**|  | [optional] 
 **confirm** | **bool**|  | [optional] 

### Return type

[**MassResponse**](MassResponse.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mass response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

