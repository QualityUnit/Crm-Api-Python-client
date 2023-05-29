# qu.crm.MinionsApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_minion**](MinionsApi.md#add_new_minion) | **POST** /minions | Add new minion
[**delete_minion**](MinionsApi.md#delete_minion) | **DELETE** /minions/{minionId} | Delete minion
[**edit_minion**](MinionsApi.md#edit_minion) | **PUT** /minions/{minionId} | Edit minion
[**get_minion**](MinionsApi.md#get_minion) | **GET** /minions/{minionId} | Minion
[**get_minion_cluster_names**](MinionsApi.md#get_minion_cluster_names) | **GET** /minions/options/clusterNames | Minion cluster names list
[**get_minion_roles**](MinionsApi.md#get_minion_roles) | **GET** /minions/options/roles | Minion roles list
[**get_minions**](MinionsApi.md#get_minions) | **GET** /minions | Minions list
[**re_sync_minion**](MinionsApi.md#re_sync_minion) | **POST** /minions/{minionId}/_reSync | Resync minion and set it up
[**set_minion_down**](MinionsApi.md#set_minion_down) | **POST** /minions/{minionId}/_setDown | Set minion down
[**set_minion_up**](MinionsApi.md#set_minion_up) | **POST** /minions/{minionId}/_setUp | Set minion up


# **add_new_minion**
> object add_new_minion(minion)

Add new minion

Add new minion

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.minion_info import MinionInfo
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
    api_instance = qu.crm.MinionsApi(api_client)
    minion = qu.crm.MinionInfo() # MinionInfo | 

    try:
        # Add new minion
        api_response = await api_instance.add_new_minion(minion)
        print("The response of MinionsApi->add_new_minion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->add_new_minion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minion** | [**MinionInfo**](MinionInfo.md)|  | 

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

# **delete_minion**
> object delete_minion(minion_id)

Delete minion

Delete minion

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
    api_instance = qu.crm.MinionsApi(api_client)
    minion_id = 'minion_id_example' # str | 

    try:
        # Delete minion
        api_response = await api_instance.delete_minion(minion_id)
        print("The response of MinionsApi->delete_minion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->delete_minion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minion_id** | **str**|  | 

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

# **edit_minion**
> object edit_minion(minion_id, minion)

Edit minion

Edit minion

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.minion_info import MinionInfo
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
    api_instance = qu.crm.MinionsApi(api_client)
    minion_id = 'minion_id_example' # str | 
    minion = qu.crm.MinionInfo() # MinionInfo | 

    try:
        # Edit minion
        api_response = await api_instance.edit_minion(minion_id, minion)
        print("The response of MinionsApi->edit_minion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->edit_minion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minion_id** | **str**|  | 
 **minion** | [**MinionInfo**](MinionInfo.md)|  | 

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

# **get_minion**
> Minion get_minion(minion_id)

Minion

Returns minion

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.minion import Minion
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
    api_instance = qu.crm.MinionsApi(api_client)
    minion_id = 'minion_id_example' # str | 

    try:
        # Minion
        api_response = await api_instance.get_minion(minion_id)
        print("The response of MinionsApi->get_minion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->get_minion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minion_id** | **str**|  | 

### Return type

[**Minion**](Minion.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_minion_cluster_names**
> List[str] get_minion_cluster_names()

Minion cluster names list

Returns list of available minion cluster names

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
    api_instance = qu.crm.MinionsApi(api_client)

    try:
        # Minion cluster names list
        api_response = await api_instance.get_minion_cluster_names()
        print("The response of MinionsApi->get_minion_cluster_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->get_minion_cluster_names: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of minion cluster names |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_minion_roles**
> List[str] get_minion_roles()

Minion roles list

Returns list of all minion roles available in db

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
    api_instance = qu.crm.MinionsApi(api_client)

    try:
        # Minion roles list
        api_response = await api_instance.get_minion_roles()
        print("The response of MinionsApi->get_minion_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->get_minion_roles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of minion roles |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_minions**
> List[Minion] get_minions(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)

Minions list

Returns lis of minions

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.minion import Minion
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
    api_instance = qu.crm.MinionsApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)
    sort_dir = 'ASC' # str | Sorting direction ASC or DESC (optional) (default to 'ASC')
    sort_field = 'sort_field_example' # str | Sorting field (optional)
    filters = 'filters_example' # str | Filters (json object {column:value, ...}) (optional)
    var_from = 56 # int | Result set start. Takes precedence over _page if defined. (optional)
    to = 56 # int | Result set end. Used only if _from is used. (optional)

    try:
        # Minions list
        api_response = await api_instance.get_minions(page=page, per_page=per_page, sort_dir=sort_dir, sort_field=sort_field, filters=filters, var_from=var_from, to=to)
        print("The response of MinionsApi->get_minions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->get_minions: %s\n" % e)
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

[**List[Minion]**](Minion.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Minion response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_sync_minion**
> object re_sync_minion(minion_id)

Resync minion and set it up

Resync minion and set it up

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
    api_instance = qu.crm.MinionsApi(api_client)
    minion_id = 'minion_id_example' # str | 

    try:
        # Resync minion and set it up
        api_response = await api_instance.re_sync_minion(minion_id)
        print("The response of MinionsApi->re_sync_minion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->re_sync_minion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minion_id** | **str**|  | 

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

# **set_minion_down**
> object set_minion_down(minion_id)

Set minion down

Set minion down

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
    api_instance = qu.crm.MinionsApi(api_client)
    minion_id = 'minion_id_example' # str | 

    try:
        # Set minion down
        api_response = await api_instance.set_minion_down(minion_id)
        print("The response of MinionsApi->set_minion_down:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->set_minion_down: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minion_id** | **str**|  | 

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

# **set_minion_up**
> object set_minion_up(minion_id)

Set minion up

Set minion up

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
    api_instance = qu.crm.MinionsApi(api_client)
    minion_id = 'minion_id_example' # str | 

    try:
        # Set minion up
        api_response = await api_instance.set_minion_up(minion_id)
        print("The response of MinionsApi->set_minion_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinionsApi->set_minion_up: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minion_id** | **str**|  | 

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

