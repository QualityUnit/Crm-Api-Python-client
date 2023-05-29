# EventLogs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**date_of_log** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.event_logs import EventLogs

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogs from a JSON string
event_logs_instance = EventLogs.from_json(json)
# print the JSON string representation of the object
print EventLogs.to_json()

# convert the object into a dict
event_logs_dict = event_logs_instance.to_dict()
# create an instance of EventLogs from a dict
event_logs_form_dict = event_logs.from_dict(event_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


