# Task


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**is_broken** | **bool** |  | [optional] 
**attempts** | [**List[TaskAttempt]**](TaskAttempt.md) |  | [optional] 
**result** | **str** | S - OK E - error R - running | [optional] 
**task_data** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


