# Setting

Single setting value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.setting import Setting

# TODO update the JSON string below
json = "{}"
# create an instance of Setting from a JSON string
setting_instance = Setting.from_json(json)
# print the JSON string representation of the object
print Setting.to_json()

# convert the object into a dict
setting_dict = setting_instance.to_dict()
# create an instance of Setting from a dict
setting_form_dict = setting.from_dict(setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


