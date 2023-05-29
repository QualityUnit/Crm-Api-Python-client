# MinionInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**cluster** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from qu.crm.models.minion_info import MinionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MinionInfo from a JSON string
minion_info_instance = MinionInfo.from_json(json)
# print the JSON string representation of the object
print MinionInfo.to_json()

# convert the object into a dict
minion_info_dict = minion_info_instance.to_dict()
# create an instance of MinionInfo from a dict
minion_info_form_dict = minion_info.from_dict(minion_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


