# TaskStepAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**scheduled_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**result** | **str** | S - OK E - error R - running | [optional] 
**error_message** | **str** |  | [optional] 
**minion_jobs** | [**List[MinionJob]**](MinionJob.md) |  | [optional] 

## Example

```python
from qu.crm.models.task_step_action import TaskStepAction

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStepAction from a JSON string
task_step_action_instance = TaskStepAction.from_json(json)
# print the JSON string representation of the object
print TaskStepAction.to_json()

# convert the object into a dict
task_step_action_dict = task_step_action_instance.to_dict()
# create an instance of TaskStepAction from a dict
task_step_action_form_dict = task_step_action.from_dict(task_step_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


