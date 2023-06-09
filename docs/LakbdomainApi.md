# qu.crm.LakbdomainApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_certificate**](LakbdomainApi.md#check_certificate) | **PUT** /lakbdomain/_check_certificate | Certificate check


# **check_certificate**
> object check_certificate(body=body)

Certificate check

Check KB domain certificate validity

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.la_kb_domain import LaKbDomain
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
    api_instance = qu.crm.LakbdomainApi(api_client)
    body = qu.crm.LaKbDomain() # LaKbDomain | LaKbDomain and certificate for validation. (optional)

    try:
        # Certificate check
        api_response = await api_instance.check_certificate(body=body)
        print("The response of LakbdomainApi->check_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LakbdomainApi->check_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LaKbDomain**](LaKbDomain.md)| LaKbDomain and certificate for validation. | [optional] 

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

