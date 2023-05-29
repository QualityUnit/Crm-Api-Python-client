# qu.crm.StatsApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_stats**](StatsApi.md#get_account_stats) | **GET** /stats/account | Account stats
[**get_agents_stats**](StatsApi.md#get_agents_stats) | **GET** /stats/agents | Agents stats for accounts with 10 or more agents
[**get_sale_stats**](StatsApi.md#get_sale_stats) | **GET** /stats/sale | Sale stats
[**get_versions_stats**](StatsApi.md#get_versions_stats) | **GET** /stats/versions | Versions stats


# **get_account_stats**
> AccountStats get_account_stats(product_family=product_family)

Account stats

Returns account stats

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.account_stats import AccountStats
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
    api_instance = qu.crm.StatsApi(api_client)
    product_family = 'product_family_example' # str |  (optional)

    try:
        # Account stats
        api_response = await api_instance.get_account_stats(product_family=product_family)
        print("The response of StatsApi->get_account_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_account_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_family** | **str**|  | [optional] 

### Return type

[**AccountStats**](AccountStats.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account stats for today |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_stats**
> AgentsStats get_agents_stats()

Agents stats for accounts with 10 or more agents

Returns agents stats

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.agents_stats import AgentsStats
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
    api_instance = qu.crm.StatsApi(api_client)

    try:
        # Agents stats for accounts with 10 or more agents
        api_response = await api_instance.get_agents_stats()
        print("The response of StatsApi->get_agents_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_agents_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AgentsStats**](AgentsStats.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agents stats for accounts with 10 or more agents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sale_stats**
> SaleStats get_sale_stats()

Sale stats

Returns sale stats

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.sale_stats import SaleStats
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
    api_instance = qu.crm.StatsApi(api_client)

    try:
        # Sale stats
        api_response = await api_instance.get_sale_stats()
        print("The response of StatsApi->get_sale_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_sale_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SaleStats**](SaleStats.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SaleStats for this quartal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions_stats**
> VersionStats get_versions_stats(product_family)

Versions stats

Returns versions stats

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.version_stats import VersionStats
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
    api_instance = qu.crm.StatsApi(api_client)
    product_family = 'product_family_example' # str | 

    try:
        # Versions stats
        api_response = await api_instance.get_versions_stats(product_family)
        print("The response of StatsApi->get_versions_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_versions_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_family** | **str**|  | 

### Return type

[**VersionStats**](VersionStats.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Versions stats for today |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

