# Addon

presence of fields 'price' and 'active' depends on the context from which addon object is returned

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codename** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**state** | **str** |  | 
**price** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from qu.crm.models.addon import Addon

# TODO update the JSON string below
json = "{}"
# create an instance of Addon from a JSON string
addon_instance = Addon.from_json(json)
# print the JSON string representation of the object
print Addon.to_json()

# convert the object into a dict
addon_dict = addon_instance.to_dict()
# create an instance of Addon from a dict
addon_form_dict = addon.from_dict(addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


