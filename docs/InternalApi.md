# qu.crm.InternalApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_user_login**](InternalApi.md#account_user_login) | **GET** /subscriptions/{subscriptionId}/_login | Login as account user
[**cancel_discount**](InternalApi.md#cancel_discount) | **DELETE** /discounts/{discountId} | Cancel discount
[**create_coupon**](InternalApi.md#create_coupon) | **POST** /coupons | Create coupon
[**create_discount**](InternalApi.md#create_discount) | **POST** /discounts | Create discount
[**custom_reseller_url**](InternalApi.md#custom_reseller_url) | **GET** /subscriptions/{subscriptionId}/upgrade_url | Custom reseller upgrade URL
[**elastic_reindex**](InternalApi.md#elastic_reindex) | **POST** /subscriptions/{subscriptionId}/elastic_reindex | Elastic reindex subscription LA data
[**elastic_reindex_status**](InternalApi.md#elastic_reindex_status) | **GET** /subscriptions/{subscriptionId}/elastic_status | LA elastic reindex status
[**generate_for_agents**](InternalApi.md#generate_for_agents) | **POST** /my-account/{subscriptionId}/_authorize | &#39;My Account&#39; token
[**get_account_users**](InternalApi.md#get_account_users) | **GET** /subscriptions/{subscriptionId}/account_users | Account users
[**get_coupons**](InternalApi.md#get_coupons) | **GET** /coupons | Coupons list
[**get_discount**](InternalApi.md#get_discount) | **GET** /discounts/{discountId} | Discount
[**get_discounts**](InternalApi.md#get_discounts) | **GET** /discounts | Discount list
[**get_outbox_email**](InternalApi.md#get_outbox_email) | **GET** /outbox/{emailId} | Email
[**get_outbox_emails**](InternalApi.md#get_outbox_emails) | **GET** /outbox | Email list
[**get_subscription_status_history**](InternalApi.md#get_subscription_status_history) | **GET** /subscriptions/{subscriptionId}/status_history | Status history
[**get_usage_breakdown**](InternalApi.md#get_usage_breakdown) | **GET** /subscriptions/{subscriptionId}/__usage_breakdown | Show usage breakdown


# **account_user_login**
> LoginUrl account_user_login(subscription_id, user_id, use_custom_domain=use_custom_domain)

Login as account user

Account user login redirect

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.login_url import LoginUrl
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
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    user_id = 'user_id_example' # str | Account user id
    use_custom_domain = False # bool | Use custom domain for login (optional) (default to False)

    try:
        # Login as account user
        api_response = await api_instance.account_user_login(subscription_id, user_id, use_custom_domain=use_custom_domain)
        print("The response of InternalApi->account_user_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->account_user_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **user_id** | **str**| Account user id | 
 **use_custom_domain** | **bool**| Use custom domain for login | [optional] [default to False]

### Return type

[**LoginUrl**](LoginUrl.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent login url |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_discount**
> object cancel_discount(discount_id, note=note)

Cancel discount

Cancel discount

### Example

* OAuth Authentication (privileges):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.InternalApi(api_client)
    discount_id = 56 # int | 
    note = 'note_example' # str |  (optional)

    try:
        # Cancel discount
        api_response = await api_instance.cancel_discount(discount_id, note=note)
        print("The response of InternalApi->cancel_discount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->cancel_discount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discount_id** | **int**|  | 
 **note** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupon**
> Coupon create_coupon(coupon)

Create coupon

Create coupon

### Example

* OAuth Authentication (privileges):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.InternalApi(api_client)
    coupon = qu.crm.Coupon() # Coupon | 

    try:
        # Create coupon
        api_response = await api_instance.create_coupon(coupon)
        print("The response of InternalApi->create_coupon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->create_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon** | [**Coupon**](Coupon.md)|  | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created coupon |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_discount**
> Discount create_discount(discount)

Create discount

Create discount

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.discount import Discount
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
    api_instance = qu.crm.InternalApi(api_client)
    discount = qu.crm.Discount() # Discount | 

    try:
        # Create discount
        api_response = await api_instance.create_discount(discount)
        print("The response of InternalApi->create_discount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->create_discount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discount** | [**Discount**](Discount.md)|  | 

### Return type

[**Discount**](Discount.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created discount |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_reseller_url**
> UpgradeUrl custom_reseller_url(subscription_id)

Custom reseller upgrade URL

Returns custom reseller upgrade URL

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.upgrade_url import UpgradeUrl
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
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Custom reseller upgrade URL
        api_response = await api_instance.custom_reseller_url(subscription_id)
        print("The response of InternalApi->custom_reseller_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->custom_reseller_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**UpgradeUrl**](UpgradeUrl.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom reseller upgrade URL |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elastic_reindex**
> object elastic_reindex(subscription_id, body=body)

Elastic reindex subscription LA data

Reindex selected subscription data ( tickets, contacts, kb ) with elastic search

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.reindex_data import ReindexData
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
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.ReindexData() # ReindexData |  (optional)

    try:
        # Elastic reindex subscription LA data
        api_response = await api_instance.elastic_reindex(subscription_id, body=body)
        print("The response of InternalApi->elastic_reindex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->elastic_reindex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**ReindexData**](ReindexData.md)|  | [optional] 

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

# **elastic_reindex_status**
> ReindexStatusData elastic_reindex_status(subscription_id)

LA elastic reindex status

Returns elastic search reindex status

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.reindex_status_data import ReindexStatusData
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
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # LA elastic reindex status
        api_response = await api_instance.elastic_reindex_status(subscription_id)
        print("The response of InternalApi->elastic_reindex_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->elastic_reindex_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**ReindexStatusData**](ReindexStatusData.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elastic reindex status |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_for_agents**
> MyAccountToken generate_for_agents(subscription_id, body=body)

'My Account' token

Generates and returns 'My Account' token for agents

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
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    body = qu.crm.MyAccountParameters() # MyAccountParameters |  (optional)

    try:
        # 'My Account' token
        api_response = await api_instance.generate_for_agents(subscription_id, body=body)
        print("The response of InternalApi->generate_for_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->generate_for_agents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
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

# **get_account_users**
> List[AccountUser] get_account_users(subscription_id)

Account users

Returns list of account users

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.account_user import AccountUser
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
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Account users
        api_response = await api_instance.get_account_users(subscription_id)
        print("The response of InternalApi->get_account_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_account_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[AccountUser]**](AccountUser.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account user list |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupons**
> List[Coupon] get_coupons()

Coupons list

Returns list of coupons

### Example

* OAuth Authentication (privileges):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.InternalApi(api_client)

    try:
        # Coupons list
        api_response = await api_instance.get_coupons()
        print("The response of InternalApi->get_coupons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_coupons: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Coupon]**](Coupon.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coupon list |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount**
> Discount get_discount(discount_id)

Discount

Returns discount

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.discount import Discount
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
    api_instance = qu.crm.InternalApi(api_client)
    discount_id = 56 # int | 

    try:
        # Discount
        api_response = await api_instance.get_discount(discount_id)
        print("The response of InternalApi->get_discount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_discount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discount_id** | **int**|  | 

### Return type

[**Discount**](Discount.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discount |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discounts**
> List[Discount] get_discounts(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Discount list

Returns list of discounts

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.discount import Discount
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
    api_instance = qu.crm.InternalApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Discount list
        api_response = await api_instance.get_discounts(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of InternalApi->get_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_discounts: %s\n" % e)
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

[**List[Discount]**](Discount.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discount list |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbox_email**
> Email get_outbox_email(email_id)

Email

Returns email in outbox

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.email import Email
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
    api_instance = qu.crm.InternalApi(api_client)
    email_id = 56 # int | 

    try:
        # Email
        api_response = await api_instance.get_outbox_email(email_id)
        print("The response of InternalApi->get_outbox_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_outbox_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **int**|  | 

### Return type

[**Email**](Email.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbox_emails**
> List[Email] get_outbox_emails(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Email list

Returns list of outbox emails

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.email import Email
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
    api_instance = qu.crm.InternalApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Email list
        api_response = await api_instance.get_outbox_emails(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of InternalApi->get_outbox_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_outbox_emails: %s\n" % e)
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

[**List[Email]**](Email.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email list |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_status_history**
> List[SubscriptionStatusHistory] get_subscription_status_history(subscription_id)

Status history

Returns subscription status history

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.subscription_status_history import SubscriptionStatusHistory
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
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Status history
        api_response = await api_instance.get_subscription_status_history(subscription_id)
        print("The response of InternalApi->get_subscription_status_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_subscription_status_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[SubscriptionStatusHistory]**](SubscriptionStatusHistory.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription status history list |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_breakdown**
> get_usage_breakdown(subscription_id)

Show usage breakdown

Displays detailed usage breakdown for current invoice

### Example

* OAuth Authentication (privileges):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with qu.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qu.crm.InternalApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Show usage breakdown
        await api_instance.get_usage_breakdown(subscription_id)
    except Exception as e:
        print("Exception when calling InternalApi->get_usage_breakdown: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | usage breakdown |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

