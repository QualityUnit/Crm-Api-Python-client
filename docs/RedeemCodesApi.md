# qu.crm.RedeemCodesApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_redeem_code**](RedeemCodesApi.md#create_redeem_code) | **POST** /redeem_codes | Create redeem code
[**get_redeem_code**](RedeemCodesApi.md#get_redeem_code) | **GET** /redeem_codes/{redeemCode} | Redeem code
[**get_redeem_codes**](RedeemCodesApi.md#get_redeem_codes) | **GET** /redeem_codes | Redeem codes list
[**redeem_code_signup**](RedeemCodesApi.md#redeem_code_signup) | **POST** /redeem_code/signup | Create subscription
[**redeem_codes_import**](RedeemCodesApi.md#redeem_codes_import) | **POST** /redeem_codes/import | Import redeem codes


# **create_redeem_code**
> RedeemCode create_redeem_code(body)

Create redeem code

Create redeem code

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.redeem_code import RedeemCode
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
    api_instance = qu.crm.RedeemCodesApi(api_client)
    body = qu.crm.RedeemCode() # RedeemCode | 

    try:
        # Create redeem code
        api_response = await api_instance.create_redeem_code(body)
        print("The response of RedeemCodesApi->create_redeem_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->create_redeem_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedeemCode**](RedeemCode.md)|  | 

### Return type

[**RedeemCode**](RedeemCode.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Redeem code |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redeem_code**
> RedeemCode get_redeem_code(redeem_code)

Redeem code

Returns redeem code

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.redeem_code import RedeemCode
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
    api_instance = qu.crm.RedeemCodesApi(api_client)
    redeem_code = 'redeem_code_example' # str | 

    try:
        # Redeem code
        api_response = await api_instance.get_redeem_code(redeem_code)
        print("The response of RedeemCodesApi->get_redeem_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->get_redeem_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redeem_code** | **str**|  | 

### Return type

[**RedeemCode**](RedeemCode.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Redeem code |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redeem_codes**
> List[RedeemCode] get_redeem_codes(page=page, per_page=per_page)

Redeem codes list

Returns list of redeem codes

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.redeem_code import RedeemCode
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
    api_instance = qu.crm.RedeemCodesApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)

    try:
        # Redeem codes list
        api_response = await api_instance.get_redeem_codes(page=page, per_page=per_page)
        print("The response of RedeemCodesApi->get_redeem_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->get_redeem_codes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Used only if _from is not defined. | [optional] 
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] 

### Return type

[**List[RedeemCode]**](RedeemCode.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Redeem codes list |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_code_signup**
> Subscription redeem_code_signup(body=body)

Create subscription

Create subscription by redeem code

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.redeem_code_signup import RedeemCodeSignup
from qu.crm.models.subscription import Subscription
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
    api_instance = qu.crm.RedeemCodesApi(api_client)
    body = qu.crm.RedeemCodeSignup() # RedeemCodeSignup |  (optional)

    try:
        # Create subscription
        api_response = await api_instance.redeem_code_signup(body=body)
        print("The response of RedeemCodesApi->redeem_code_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->redeem_code_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedeemCodeSignup**](RedeemCodeSignup.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_codes_import**
> MassResponse redeem_codes_import(codes=codes)

Import redeem codes

Import redeem codes

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.mass_response import MassResponse
from qu.crm.models.redeem_codes_import import RedeemCodesImport
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
    api_instance = qu.crm.RedeemCodesApi(api_client)
    codes = qu.crm.RedeemCodesImport() # RedeemCodesImport |  (optional)

    try:
        # Import redeem codes
        api_response = await api_instance.redeem_codes_import(codes=codes)
        print("The response of RedeemCodesApi->redeem_codes_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->redeem_codes_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codes** | [**RedeemCodesImport**](RedeemCodesImport.md)|  | [optional] 

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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

