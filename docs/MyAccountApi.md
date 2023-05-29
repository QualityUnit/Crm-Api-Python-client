# qu.crm.MyAccountApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_stop**](MyAccountApi.md#cancel_stop) | **POST** /my-account/_cancelStop | Restart billing
[**change_addons_for_my_account**](MyAccountApi.md#change_addons_for_my_account) | **PUT** /my-account/addons | Addon change
[**download_invoice_for_my_account**](MyAccountApi.md#download_invoice_for_my_account) | **GET** /my-account/invoices/{invoiceNumber}/_download | Download invoice
[**download_summary**](MyAccountApi.md#download_summary) | **GET** /my-account/summary/{orderNumber}/_download | Downloads summary
[**generate**](MyAccountApi.md#generate) | **POST** /checkout/_authorize | &#39;My Account&#39; token
[**get_account_invoices**](MyAccountApi.md#get_account_invoices) | **GET** /my-account/invoices | Invoices list
[**get_account_summaries**](MyAccountApi.md#get_account_summaries) | **GET** /my-account/summary/history | Summaries list
[**get_active_addons_for_my_account**](MyAccountApi.md#get_active_addons_for_my_account) | **GET** /my-account/addons | Plan addons list
[**get_agents_count**](MyAccountApi.md#get_agents_count) | **GET** /my-account/usage/agents/count | Agents count
[**get_all_variation_addons_for_my_account**](MyAccountApi.md#get_all_variation_addons_for_my_account) | **GET** /my-account/variations/{variationId}/addons | Variations addons
[**get_billing_info_for_my_account**](MyAccountApi.md#get_billing_info_for_my_account) | **GET** /my-account/billingInfo | Billing info
[**get_billing_status_for_my_account**](MyAccountApi.md#get_billing_status_for_my_account) | **GET** /my-account/billingStatus | Billing status
[**get_coupon_for_my_account**](MyAccountApi.md#get_coupon_for_my_account) | **GET** /my-account/coupons/{couponCode} | Coupon
[**get_knowledgebases_count**](MyAccountApi.md#get_knowledgebases_count) | **GET** /my-account/usage/knowledgebases/count | Knowledgebases count
[**get_payment_method_for_my_account**](MyAccountApi.md#get_payment_method_for_my_account) | **GET** /my-account/paymentMethod | Get Payment method
[**get_payment_processor_for_my_account**](MyAccountApi.md#get_payment_processor_for_my_account) | **GET** /my-account/paymentProcessor | Payment processor
[**get_subscription_for_my_account**](MyAccountApi.md#get_subscription_for_my_account) | **GET** /my-account/subscription | Subscription
[**get_summary_for_my_account**](MyAccountApi.md#get_summary_for_my_account) | **GET** /my-account/summary | Current period summary
[**get_upgrade_variations_for_my_account**](MyAccountApi.md#get_upgrade_variations_for_my_account) | **GET** /my-account/upgradeVariations | Upgrade variation list
[**get_variation_for_my_account**](MyAccountApi.md#get_variation_for_my_account) | **GET** /my-account/variation | Variation
[**parameters**](MyAccountApi.md#parameters) | **GET** /my-account/parameters | &#39;My Account&#39; parameters
[**predict_price**](MyAccountApi.md#predict_price) | **POST** /my-account/_predictPrice | Returns list of items and predicted price
[**send_payment_error**](MyAccountApi.md#send_payment_error) | **POST** /my-account/sendPaymentError | Sends payment error to server
[**stop_account**](MyAccountApi.md#stop_account) | **POST** /my-account/_stop | Stop billing
[**update_billing_info**](MyAccountApi.md#update_billing_info) | **PUT** /my-account/billingInfo | Billing info
[**update_payment_method**](MyAccountApi.md#update_payment_method) | **PUT** /my-account/paymentMethod | Update payment method
[**upgrade_plan**](MyAccountApi.md#upgrade_plan) | **POST** /my-account/_upgrade | Change plan
[**validate_billing_info_for_my_account**](MyAccountApi.md#validate_billing_info_for_my_account) | **POST** /my-account/_validateBillingInfo | Test Billing info


# **cancel_stop**
> object cancel_stop(checkout_token, reason=reason)

Restart billing

Restarts billing

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.message import Message
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    reason = qu.crm.Message() # Message | Reason for restarting (optional)

    try:
        # Restart billing
        api_response = await api_instance.cancel_stop(checkout_token, reason=reason)
        print("The response of MyAccountApi->cancel_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->cancel_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **reason** | [**Message**](Message.md)| Reason for restarting | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_addons_for_my_account**
> List[Addon] change_addons_for_my_account(checkout_token, body=body)

Addon change

Change active subscription addons

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.addon import Addon
from qu.crm.models.addon_list import AddonList
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    body = qu.crm.AddonList() # AddonList |  (optional)

    try:
        # Addon change
        api_response = await api_instance.change_addons_for_my_account(checkout_token, body=body)
        print("The response of MyAccountApi->change_addons_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->change_addons_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **body** | [**AddonList**](AddonList.md)|  | [optional] 

### Return type

[**List[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New subscription addons list (without price field) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_invoice_for_my_account**
> bytearray download_invoice_for_my_account(checkout_token, invoice_number)

Download invoice

Downloads invoice

### Example

```python
import time
import os
import qu.crm
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    invoice_number = 'invoice_number_example' # str | 

    try:
        # Download invoice
        api_response = await api_instance.download_invoice_for_my_account(checkout_token, invoice_number)
        print("The response of MyAccountApi->download_invoice_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->download_invoice_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **invoice_number** | **str**|  | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice in pdf format |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_summary**
> bytearray download_summary(checkout_token, order_number)

Downloads summary

Downloads summary

### Example

```python
import time
import os
import qu.crm
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    order_number = 'order_number_example' # str | 

    try:
        # Downloads summary
        api_response = await api_instance.download_summary(checkout_token, order_number)
        print("The response of MyAccountApi->download_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->download_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **order_number** | **str**|  | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary in pdf format |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate**
> MyAccountToken generate(body=body)

'My Account' token

Generates and returns 'My Account' token

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.my_account_parameters import MyAccountParameters
from qu.crm.models.my_account_token import MyAccountToken
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
    api_instance = qu.crm.MyAccountApi(api_client)
    body = qu.crm.MyAccountParameters() # MyAccountParameters |  (optional)

    try:
        # 'My Account' token
        api_response = await api_instance.generate(body=body)
        print("The response of MyAccountApi->generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->generate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MyAccountParameters**](MyAccountParameters.md)|  | [optional] 

### Return type

[**MyAccountToken**](MyAccountToken.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | &#39;My Account&#39; token |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_invoices**
> List[Invoice] get_account_invoices(checkout_token, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Invoices list

Returns list of invoices

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.invoice import Invoice
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Invoices list
        api_response = await api_instance.get_account_invoices(checkout_token, page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of MyAccountApi->get_account_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_account_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **page** | **int**| Page to display. Used only if _from is not defined. | [optional] 
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] 
 **sort_dir** | **str**| Sorting direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| Sorting field | [optional] 
 **filters** | **str**| Filters (json object {column:value, ...}) | [optional] 
 **var_from** | **int**| Result set start. Takes precedence over _page if defined. | [optional] 
 **to** | **int**| Result set end. Used only if _from is used. | [optional] 

### Return type

[**List[Invoice]**](Invoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoices response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_summaries**
> List[SummaryHistoryItem] get_account_summaries(checkout_token)

Summaries list

Returns list of summaries

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.summary_history_item import SummaryHistoryItem
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Summaries list
        api_response = await api_instance.get_account_summaries(checkout_token)
        print("The response of MyAccountApi->get_account_summaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_account_summaries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**List[SummaryHistoryItem]**](SummaryHistoryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summaries response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_addons_for_my_account**
> List[Addon] get_active_addons_for_my_account(checkout_token)

Plan addons list

Returns list of active plan addons

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.addon import Addon
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Plan addons list
        api_response = await api_instance.get_active_addons_for_my_account(checkout_token)
        print("The response of MyAccountApi->get_active_addons_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_active_addons_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**List[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plan addons list (without price field) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_count**
> AgentsCount get_agents_count(checkout_token)

Agents count

Returns agents count

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.agents_count import AgentsCount
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Agents count
        api_response = await api_instance.get_agents_count(checkout_token)
        print("The response of MyAccountApi->get_agents_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_agents_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**AgentsCount**](AgentsCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agents count |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_variation_addons_for_my_account**
> List[Addon] get_all_variation_addons_for_my_account(variation_id, checkout_token)

Variations addons

Returns all addons related to specified variation.

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.addon import Addon
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
    api_instance = qu.crm.MyAccountApi(api_client)
    variation_id = 'variation_id_example' # str | 
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Variations addons
        api_response = await api_instance.get_all_variation_addons_for_my_account(variation_id, checkout_token)
        print("The response of MyAccountApi->get_all_variation_addons_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_all_variation_addons_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variation_id** | **str**|  | 
 **checkout_token** | **str**|  | 

### Return type

[**List[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Variation addons response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_info_for_my_account**
> Customer get_billing_info_for_my_account(checkout_token)

Billing info

Returns billing info

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.customer import Customer
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Billing info
        api_response = await api_instance.get_billing_info_for_my_account(checkout_token)
        print("The response of MyAccountApi->get_billing_info_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_billing_info_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_status_for_my_account**
> BillingStatus get_billing_status_for_my_account(checkout_token)

Billing status

Returns billing status

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.billing_status import BillingStatus
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Billing status
        api_response = await api_instance.get_billing_status_for_my_account(checkout_token)
        print("The response of MyAccountApi->get_billing_status_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_billing_status_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**BillingStatus**](BillingStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing status |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_for_my_account**
> Coupon get_coupon_for_my_account(checkout_token, coupon_code, billing_period)

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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    coupon_code = 'coupon_code_example' # str | 
    billing_period = 'billing_period_example' # str | 

    try:
        # Coupon
        api_response = await api_instance.get_coupon_for_my_account(checkout_token, coupon_code, billing_period)
        print("The response of MyAccountApi->get_coupon_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_coupon_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **coupon_code** | **str**|  | 
 **billing_period** | **str**|  | 

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

# **get_knowledgebases_count**
> KnowledgebasesCount get_knowledgebases_count(checkout_token)

Knowledgebases count

Returns knowledgebases count

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.knowledgebases_count import KnowledgebasesCount
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Knowledgebases count
        api_response = await api_instance.get_knowledgebases_count(checkout_token)
        print("The response of MyAccountApi->get_knowledgebases_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_knowledgebases_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**KnowledgebasesCount**](KnowledgebasesCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledgebases count |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_for_my_account**
> PaymentInfo get_payment_method_for_my_account(checkout_token)

Get Payment method

Returns payment method

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.payment_info import PaymentInfo
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Get Payment method
        api_response = await api_instance.get_payment_method_for_my_account(checkout_token)
        print("The response of MyAccountApi->get_payment_method_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_payment_method_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**PaymentInfo**](PaymentInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment method info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_processor_for_my_account**
> PaymentProcessorType get_payment_processor_for_my_account(checkout_token, payment_type, country=country)

Payment processor

Returns payment processor to use when updating payment method

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.payment_processor_type import PaymentProcessorType
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    payment_type = 'payment_type_example' # str | 
    country = 'country_example' # str |  (optional)

    try:
        # Payment processor
        api_response = await api_instance.get_payment_processor_for_my_account(checkout_token, payment_type, country=country)
        print("The response of MyAccountApi->get_payment_processor_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_payment_processor_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **payment_type** | **str**|  | 
 **country** | **str**|  | [optional] 

### Return type

[**PaymentProcessorType**](PaymentProcessorType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment processor type |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_for_my_account**
> Subscription get_subscription_for_my_account(checkout_token)

Subscription

Returns subscription

### Example

```python
import time
import os
import qu.crm
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Subscription
        api_response = await api_instance.get_subscription_for_my_account(checkout_token)
        print("The response of MyAccountApi->get_subscription_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_subscription_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_for_my_account**
> Summary get_summary_for_my_account(checkout_token)

Current period summary

Returns summary of the current billing period for subscription

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.summary import Summary
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Current period summary
        api_response = await api_instance.get_summary_for_my_account(checkout_token)
        print("The response of MyAccountApi->get_summary_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_summary_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**Summary**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing summary |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_variations_for_my_account**
> VariationUpgrades get_upgrade_variations_for_my_account(checkout_token, country=country, vat_id=vat_id)

Upgrade variation list

Returns list of variations user can upgrade to and their current variation

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.variation_upgrades import VariationUpgrades
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    country = 'country_example' # str |  (optional)
    vat_id = 'vat_id_example' # str |  (optional)

    try:
        # Upgrade variation list
        api_response = await api_instance.get_upgrade_variations_for_my_account(checkout_token, country=country, vat_id=vat_id)
        print("The response of MyAccountApi->get_upgrade_variations_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_upgrade_variations_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **country** | **str**|  | [optional] 
 **vat_id** | **str**|  | [optional] 

### Return type

[**VariationUpgrades**](VariationUpgrades.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available upgrades response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variation_for_my_account**
> Variation get_variation_for_my_account(checkout_token)

Variation

Returns variation

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.variation import Variation
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # Variation
        api_response = await api_instance.get_variation_for_my_account(checkout_token)
        print("The response of MyAccountApi->get_variation_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_variation_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**Variation**](Variation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Variation response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters**
> MyAccountParameters parameters(checkout_token)

'My Account' parameters

Returns 'My Account' parameters

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.my_account_parameters import MyAccountParameters
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 

    try:
        # 'My Account' parameters
        api_response = await api_instance.parameters(checkout_token)
        print("The response of MyAccountApi->parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 

### Return type

[**MyAccountParameters**](MyAccountParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | &#39;My Account&#39; parameters |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_price**
> CalculatedItems predict_price(checkout_token, body=body)

Returns list of items and predicted price

Returns list of items and predicted price

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.billing_parameters import BillingParameters
from qu.crm.models.calculated_items import CalculatedItems
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    body = qu.crm.BillingParameters() # BillingParameters |  (optional)

    try:
        # Returns list of items and predicted price
        api_response = await api_instance.predict_price(checkout_token, body=body)
        print("The response of MyAccountApi->predict_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->predict_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **body** | [**BillingParameters**](BillingParameters.md)|  | [optional] 

### Return type

[**CalculatedItems**](CalculatedItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Items calculated for selected plan |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_payment_error**
> object send_payment_error(checkout_token, body=body)

Sends payment error to server

Sends payment error to server

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.payment_error_info import PaymentErrorInfo
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    body = qu.crm.PaymentErrorInfo() # PaymentErrorInfo |  (optional)

    try:
        # Sends payment error to server
        api_response = await api_instance.send_payment_error(checkout_token, body=body)
        print("The response of MyAccountApi->send_payment_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->send_payment_error: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **body** | [**PaymentErrorInfo**](PaymentErrorInfo.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_account**
> object stop_account(checkout_token, reason=reason)

Stop billing

Stops account

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.message import Message
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    reason = qu.crm.Message() # Message | Reason for stopping (optional)

    try:
        # Stop billing
        api_response = await api_instance.stop_account(checkout_token, reason=reason)
        print("The response of MyAccountApi->stop_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->stop_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **reason** | [**Message**](Message.md)| Reason for stopping | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_info**
> object update_billing_info(checkout_token, body=body)

Billing info

Updates billing info

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.billing_info import BillingInfo
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    body = qu.crm.BillingInfo() # BillingInfo |  (optional)

    try:
        # Billing info
        api_response = await api_instance.update_billing_info(checkout_token, body=body)
        print("The response of MyAccountApi->update_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->update_billing_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **body** | [**BillingInfo**](BillingInfo.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> PaymentInfo update_payment_method(checkout_token, body=body)

Update payment method

Updates payment method

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.payment_info import PaymentInfo
from qu.crm.models.payment_method import PaymentMethod
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    body = qu.crm.PaymentMethod() # PaymentMethod |  (optional)

    try:
        # Update payment method
        api_response = await api_instance.update_payment_method(checkout_token, body=body)
        print("The response of MyAccountApi->update_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->update_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **body** | [**PaymentMethod**](PaymentMethod.md)|  | [optional] 

### Return type

[**PaymentInfo**](PaymentInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New payment method info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_plan**
> object upgrade_plan(checkout_token, body=body)

Change plan

Upgrades subscription to another variation method. In case of upgrade from paid to paid, it's possible to change country without changing payment method. If change is between EU and not EU, different payment rules might apply

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.upgrade import Upgrade
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    body = qu.crm.Upgrade() # Upgrade |  (optional)

    try:
        # Change plan
        api_response = await api_instance.upgrade_plan(checkout_token, body=body)
        print("The response of MyAccountApi->upgrade_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->upgrade_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **body** | [**Upgrade**](Upgrade.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**201** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_billing_info_for_my_account**
> object validate_billing_info_for_my_account(checkout_token, body=body)

Test Billing info

Checks if billing info can be updated without issues. Field 'force' in BillingInfo is ignored in this call

### Example

```python
import time
import os
import qu.crm
from qu.crm.models.billing_info import BillingInfo
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
    api_instance = qu.crm.MyAccountApi(api_client)
    checkout_token = 'checkout_token_example' # str | 
    body = qu.crm.BillingInfo() # BillingInfo |  (optional)

    try:
        # Test Billing info
        api_response = await api_instance.validate_billing_info_for_my_account(checkout_token, body=body)
        print("The response of MyAccountApi->validate_billing_info_for_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->validate_billing_info_for_my_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_token** | **str**|  | 
 **body** | [**BillingInfo**](BillingInfo.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**403** | When provided billing info is valid, but updating would cause payment method to be removed because of deprecation. |  -  |
**404** | When some parts of provided billing info are missing or invalid. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

