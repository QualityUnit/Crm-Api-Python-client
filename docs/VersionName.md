# VersionName


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_stable** | **bool** |  | [optional] 

## Example

```python
from qu.crm.models.version_name import VersionName

# TODO update the JSON string below
json = "{}"
# create an instance of VersionName from a JSON string
version_name_instance = VersionName.from_json(json)
# print the JSON string representation of the object
print VersionName.to_json()

# convert the object into a dict
version_name_dict = version_name_instance.to_dict()
# create an instance of VersionName from a dict
version_name_form_dict = version_name.from_dict(version_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


