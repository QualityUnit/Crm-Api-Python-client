# qu.crm.RefundsApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_refund**](RefundsApi.md#get_refund) | **GET** /refunds/{refundId} | Refund
[**get_refunds**](RefundsApi.md#get_refunds) | **GET** /refunds | Refund list


# **get_refund**
> Refund get_refund(refund_id)

Refund

Get refund

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.refund import Refund
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
    api_instance = qu.crm.RefundsApi(api_client)
    refund_id = 56 # int | 

    try:
        # Refund
        api_response = await api_instance.get_refund(refund_id)
        print("The response of RefundsApi->get_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundsApi->get_refund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **int**|  | 

### Return type

[**Refund**](Refund.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refund response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refunds**
> List[Refund] get_refunds(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Refund list

Refund list

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.refund import Refund
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
    api_instance = qu.crm.RefundsApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Refund list
        api_response = await api_instance.get_refunds(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of RefundsApi->get_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundsApi->get_refunds: %s\n" % e)
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

[**List[Refund]**](Refund.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refunds response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

