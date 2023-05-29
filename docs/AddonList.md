# AddonList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | **List[str]** | addon codenames | 

## Example

```python
from qu.crm.models.addon_list import AddonList

# TODO update the JSON string below
json = "{}"
# create an instance of AddonList from a JSON string
addon_list_instance = AddonList.from_json(json)
# print the JSON string representation of the object
print AddonList.to_json()

# convert the object into a dict
addon_list_dict = addon_list_instance.to_dict()
# create an instance of AddonList from a dict
addon_list_form_dict = addon_list.from_dict(addon_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


