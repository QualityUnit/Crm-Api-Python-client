# qu.crm.CouponsApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extend_coupon_validity**](CouponsApi.md#extend_coupon_validity) | **POST** /coupons/{couponCode}/_extend_validity | Extend coupon validity


# **extend_coupon_validity**
> object extend_coupon_validity(coupon_code, body=body)

Extend coupon validity

Extend coupon validity

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.validity_extension import ValidityExtension
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
    api_instance = qu.crm.CouponsApi(api_client)
    coupon_code = 'coupon_code_example' # str | 
    body = qu.crm.ValidityExtension() # ValidityExtension |  (optional)

    try:
        # Extend coupon validity
        api_response = await api_instance.extend_coupon_validity(coupon_code, body=body)
        print("The response of CouponsApi->extend_coupon_validity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->extend_coupon_validity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**|  | 
 **body** | [**ValidityExtension**](ValidityExtension.md)|  | [optional] 

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

