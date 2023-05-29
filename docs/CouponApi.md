# qu.crm.CouponApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coupon**](CouponApi.md#get_coupon) | **GET** /coupons/{couponCode} | Coupon


# **get_coupon**
> Coupon get_coupon(coupon_code)

Coupon

Returns coupon

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.coupon import Coupon
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
    api_instance = qu.crm.CouponApi(api_client)
    coupon_code = 'coupon_code_example' # str | 

    try:
        # Coupon
        api_response = await api_instance.get_coupon(coupon_code)
        print("The response of CouponApi->get_coupon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponApi->get_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**|  | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coupon |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

