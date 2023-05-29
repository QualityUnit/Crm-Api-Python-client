# qu.crm.TokenApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](TokenApi.md#get_access_token) | **POST** /token | Access token


# **get_access_token**
> Token get_access_token(body=body)

Access token

Returns access token

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.credentials import Credentials
from qu.crm.models.token import Token
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
    api_instance = qu.crm.TokenApi(api_client)
    body = qu.crm.Credentials() # Credentials |  (optional)

    try:
        # Access token
        api_response = await api_instance.get_access_token(body=body)
        print("The response of TokenApi->get_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->get_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Credentials**](Credentials.md)|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | access token |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

