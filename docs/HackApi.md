# qu.crm.HackApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hack_dummy_payment_method**](HackApi.md#hack_dummy_payment_method) | **POST** /_hack/_dummy_payment_method | Set dummy payment method


# **hack_dummy_payment_method**
> object hack_dummy_payment_method(body=body)

Set dummy payment method

Set dummy payment info

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.hack_dummy_payment import HackDummyPayment
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
    api_instance = qu.crm.HackApi(api_client)
    body = qu.crm.HackDummyPayment() # HackDummyPayment |  (optional)

    try:
        # Set dummy payment method
        api_response = await api_instance.hack_dummy_payment_method(body=body)
        print("The response of HackApi->hack_dummy_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HackApi->hack_dummy_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HackDummyPayment**](HackDummyPayment.md)|  | [optional] 

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

