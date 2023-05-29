# TaskAttempt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**task_id** | **str** |  | [optional] 
**is_broken** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**task_data** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**result** | **str** | S - OK E - error R - running | [optional] 
**retried_by** | **str** |  | [optional] 
**steps** | [**List[TaskStep]**](TaskStep.md) |  | [optional] 

## Example

```python
from qu.crm.models.task_attempt import TaskAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAttempt from a JSON string
task_attempt_instance = TaskAttempt.from_json(json)
# print the JSON string representation of the object
print TaskAttempt.to_json()

# convert the object into a dict
task_attempt_dict = task_attempt_instance.to_dict()
# create an instance of TaskAttempt from a dict
task_attempt_form_dict = task_attempt.from_dict(task_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


