# MinionJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** |  | 
**minion_id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**salt_jid** | **str** |  | [optional] 
**scheduled_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**result** | **str** | S - OK E - error R - running N - not scheduled | [optional] 
**result_body** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.minion_job import MinionJob

# TODO update the JSON string below
json = "{}"
# create an instance of MinionJob from a JSON string
minion_job_instance = MinionJob.from_json(json)
# print the JSON string representation of the object
print MinionJob.to_json()

# convert the object into a dict
minion_job_dict = minion_job_instance.to_dict()
# create an instance of MinionJob from a dict
minion_job_form_dict = minion_job.from_dict(minion_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


