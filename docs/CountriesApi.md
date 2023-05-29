# qu.crm.CountriesApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](CountriesApi.md#get_countries) | **GET** /countries | Country list


# **get_countries**
> List[Country] get_countries()

Country list

Returns list of available countries

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.country import Country
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
    api_instance = qu.crm.CountriesApi(api_client)

    try:
        # Country list
        api_response = await api_instance.get_countries()
        print("The response of CountriesApi->get_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_countries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Country]**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Country list |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

