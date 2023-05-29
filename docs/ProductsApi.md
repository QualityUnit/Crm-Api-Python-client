# qu.crm.ProductsApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_version**](ProductsApi.md#create_product_version) | **POST** /products/{productId}/versions | Create new product version
[**delete_product_version**](ProductsApi.md#delete_product_version) | **DELETE** /products/{productId}/versions/{productVersionName} | Delete product version
[**get_all_product_available_versions**](ProductsApi.md#get_all_product_available_versions) | **GET** /products/{productId}/available_versions | Product available versions
[**get_product**](ProductsApi.md#get_product) | **GET** /products/{productId} | Product
[**get_product_version**](ProductsApi.md#get_product_version) | **GET** /products/{productId}/versions/{productVersionName} | Product version
[**get_product_versions**](ProductsApi.md#get_product_versions) | **GET** /products/{productId}/versions | Product versions
[**get_products**](ProductsApi.md#get_products) | **GET** /products | Products list
[**mark_product_version_for_deletion**](ProductsApi.md#mark_product_version_for_deletion) | **PUT** /products/{productId}/versions/{productVersionName}/mark_for_deletion | Mark product version for deletion
[**update_product_version**](ProductsApi.md#update_product_version) | **PUT** /products/{productId}/versions/{productVersionName} | Update product version


# **create_product_version**
> ProductVersion create_product_version(product_id, version)

Create new product version

Create new product version

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.product_version import ProductVersion
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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 
    version = qu.crm.ProductVersion() # ProductVersion | 

    try:
        # Create new product version
        api_response = await api_instance.create_product_version(product_id, version)
        print("The response of ProductsApi->create_product_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->create_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **version** | [**ProductVersion**](ProductVersion.md)|  | 

### Return type

[**ProductVersion**](ProductVersion.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product version response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_version**
> object delete_product_version(product_id, product_version_name)

Delete product version

Delete product version

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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 
    product_version_name = 'product_version_name_example' # str | 

    try:
        # Delete product version
        api_response = await api_instance.delete_product_version(product_id, product_version_name)
        print("The response of ProductsApi->delete_product_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->delete_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **product_version_name** | **str**|  | 

### Return type

**object**

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_product_available_versions**
> List[VersionName] get_all_product_available_versions(product_id, account_version)

Product available versions

Get all product available versions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.version_name import VersionName
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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 
    account_version = 'account_version_example' # str | 

    try:
        # Product available versions
        api_response = await api_instance.get_all_product_available_versions(product_id, account_version)
        print("The response of ProductsApi->get_all_product_available_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_all_product_available_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **account_version** | **str**|  | 

### Return type

[**List[VersionName]**](VersionName.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product version response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(product_id)

Product

Returns product

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.product import Product
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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Product
        api_response = await api_instance.get_product(product_id)
        print("The response of ProductsApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

[**Product**](Product.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_version**
> ProductVersion get_product_version(product_id, product_version_name)

Product version

Get product version

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.product_version import ProductVersion
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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 
    product_version_name = 'product_version_name_example' # str | 

    try:
        # Product version
        api_response = await api_instance.get_product_version(product_id, product_version_name)
        print("The response of ProductsApi->get_product_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **product_version_name** | **str**|  | 

### Return type

[**ProductVersion**](ProductVersion.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product version response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_versions**
> List[ProductVersion] get_product_versions(product_id)

Product versions

Get product versions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.product_version import ProductVersion
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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        # Product versions
        api_response = await api_instance.get_product_versions(product_id)
        print("The response of ProductsApi->get_product_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

[**List[ProductVersion]**](ProductVersion.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product version response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> List[Product] get_products(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Products list

Returns list of products

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.product import Product
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
    api_instance = qu.crm.ProductsApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Products list
        api_response = await api_instance.get_products(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of ProductsApi->get_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_products: %s\n" % e)
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

[**List[Product]**](Product.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_product_version_for_deletion**
> object mark_product_version_for_deletion(product_id, product_version_name, version)

Mark product version for deletion

Mark product version for deletion

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.deletion_marker import DeletionMarker
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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 
    product_version_name = 'product_version_name_example' # str | 
    version = qu.crm.DeletionMarker() # DeletionMarker | 

    try:
        # Mark product version for deletion
        api_response = await api_instance.mark_product_version_for_deletion(product_id, product_version_name, version)
        print("The response of ProductsApi->mark_product_version_for_deletion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->mark_product_version_for_deletion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **product_version_name** | **str**|  | 
 **version** | [**DeletionMarker**](DeletionMarker.md)|  | 

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

# **update_product_version**
> ProductVersion update_product_version(product_id, product_version_name, version)

Update product version

Update product version

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.product_version import ProductVersion
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
    api_instance = qu.crm.ProductsApi(api_client)
    product_id = 'product_id_example' # str | 
    product_version_name = 'product_version_name_example' # str | 
    version = qu.crm.ProductVersion() # ProductVersion | 

    try:
        # Update product version
        api_response = await api_instance.update_product_version(product_id, product_version_name, version)
        print("The response of ProductsApi->update_product_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->update_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **product_version_name** | **str**|  | 
 **version** | [**ProductVersion**](ProductVersion.md)|  | 

### Return type

[**ProductVersion**](ProductVersion.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product version response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

