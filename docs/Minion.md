# Minion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**cluster** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**up_date** | **datetime** |  | [optional] 
**down_date** | **datetime** |  | [optional] 
**goingup_date** | **datetime** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from qu.crm.models.minion import Minion

# TODO update the JSON string below
json = "{}"
# create an instance of Minion from a JSON string
minion_instance = Minion.from_json(json)
# print the JSON string representation of the object
print Minion.to_json()

# convert the object into a dict
minion_dict = minion_instance.to_dict()
# create an instance of Minion from a dict
minion_form_dict = minion.from_dict(minion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


