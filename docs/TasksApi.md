# qu.crm.TasksApi

All URIs are relative to *https://crm.qualityunit.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rich_task**](TasksApi.md#get_rich_task) | **GET** /executor/tasks/{taskId} | Task
[**get_rich_task_attempt**](TasksApi.md#get_rich_task_attempt) | **GET** /executor/task_attempts/{taskAttemptId} | Task attempt
[**get_task_action**](TasksApi.md#get_task_action) | **GET** /executor/actions/{actionId} | Action
[**get_task_minion_job**](TasksApi.md#get_task_minion_job) | **GET** /executor/actions/{actionId}/minion_jobs/{minionId} | Minion job
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /executor/tasks | List of tasks
[**mark_task_broken**](TasksApi.md#mark_task_broken) | **POST** /executor/tasks/{taskId}/_mark_broken | Mark task broken
[**retry_task_attempt**](TasksApi.md#retry_task_attempt) | **POST** /executor/tasks/{taskAttemptId}/_retry | Retry task attempt


# **get_rich_task**
> Task get_rich_task(task_id)

Task

Returns task

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.task import Task
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
    api_instance = qu.crm.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Task
        api_response = await api_instance.get_rich_task(task_id)
        print("The response of TasksApi->get_rich_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_rich_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rich task response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rich_task_attempt**
> TaskAttempt get_rich_task_attempt(task_attempt_id)

Task attempt

Returns task attempt

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.task_attempt import TaskAttempt
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
    api_instance = qu.crm.TasksApi(api_client)
    task_attempt_id = 'task_attempt_id_example' # str | 

    try:
        # Task attempt
        api_response = await api_instance.get_rich_task_attempt(task_attempt_id)
        print("The response of TasksApi->get_rich_task_attempt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_rich_task_attempt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_attempt_id** | **str**|  | 

### Return type

[**TaskAttempt**](TaskAttempt.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rich task attempt response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_action**
> TaskStepAction get_task_action(action_id)

Action

Returns action

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.task_step_action import TaskStepAction
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
    api_instance = qu.crm.TasksApi(api_client)
    action_id = 'action_id_example' # str | 

    try:
        # Action
        api_response = await api_instance.get_task_action(action_id)
        print("The response of TasksApi->get_task_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 

### Return type

[**TaskStepAction**](TaskStepAction.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rich action response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_minion_job**
> MinionJob get_task_minion_job(action_id, minion_id)

Minion job

Returns minion job

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.minion_job import MinionJob
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
    api_instance = qu.crm.TasksApi(api_client)
    action_id = 'action_id_example' # str | 
    minion_id = 'minion_id_example' # str | 

    try:
        # Minion job
        api_response = await api_instance.get_task_minion_job(action_id, minion_id)
        print("The response of TasksApi->get_task_minion_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_minion_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 
 **minion_id** | **str**|  | 

### Return type

[**MinionJob**](MinionJob.md)

### Authorization

[privileges](../README.md#privileges)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rich minion job response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> List[TaskAttempt] get_tasks(page=page, per_page=per_page)

List of tasks

Returns list of tasks

### Example

* OAuth Authentication (privileges):
```python
import time
import os
import qu.crm
from qu.crm.models.task_attempt import TaskAttempt
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
    api_instance = qu.crm.TasksApi(api_client)
    page = 56 # int | Page to display. Used only if _from is not defined. (optional)
    per_page = 56 # int | Results per page. Used only if _page is used. (optional)

    try:
        # List of tasks
        api_response = await api_instance.get_tasks(page=page, per_page=per_page)
        print("The response of TasksApi->get_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page to display. Used only if _from is not defined. | [optional] 
 **per_page** | **int**| Results per page. Used only if _page is used. | [optional] 

### Return type

[**List[TaskAttempt]**](TaskAttempt.md)

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

# **mark_task_broken**
> object mark_task_broken(task_id)

Mark task broken

Mark task broken

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
    api_instance = qu.crm.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Mark task broken
        api_response = await api_instance.mark_task_broken(task_id)
        print("The response of TasksApi->mark_task_broken:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->mark_task_broken: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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

# **retry_task_attempt**
> object retry_task_attempt(task_attempt_id)

Retry task attempt

Retry task attempt

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
    api_instance = qu.crm.TasksApi(api_client)
    task_attempt_id = 'task_attempt_id_example' # str | 

    try:
        # Retry task attempt
        api_response = await api_instance.retry_task_attempt(task_attempt_id)
        print("The response of TasksApi->retry_task_attempt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->retry_task_attempt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_attempt_id** | **str**|  | 

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

