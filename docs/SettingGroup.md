# SettingGroup

Setting group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Setting]**](Setting.md) | Setting group | [optional] 

## Example

```python
from qu.crm.models.setting_group import SettingGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SettingGroup from a JSON string
setting_group_instance = SettingGroup.from_json(json)
# print the JSON string representation of the object
print SettingGroup.to_json()

# convert the object into a dict
setting_group_dict = setting_group_instance.to_dict()
# create an instance of SettingGroup from a dict
setting_group_form_dict = setting_group.from_dict(setting_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


