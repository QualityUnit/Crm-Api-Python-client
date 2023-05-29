# qu.crm.LiveagentApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_knowledgebases**](LiveagentApi.md#set_knowledgebases) | **POST** /subscriptions/{subscriptionId}/liveagent/knowledgebases | Set knowledgebase settings


# **set_knowledgebases**
> object set_knowledgebases(subscription_id, knowledgebases=knowledgebases)

Set knowledgebase settings

Set knowledgebase settings

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.la_kb_collection import LaKbCollection
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
    api_instance = qu.crm.LiveagentApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    knowledgebases = qu.crm.LaKbCollection() # LaKbCollection |  (optional)

    try:
        # Set knowledgebase settings
        api_response = await api_instance.set_knowledgebases(subscription_id, knowledgebases=knowledgebases)
        print("The response of LiveagentApi->set_knowledgebases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveagentApi->set_knowledgebases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **knowledgebases** | [**LaKbCollection**](LaKbCollection.md)|  | [optional] 

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

