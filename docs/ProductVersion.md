# ProductVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**release_date** | **date** |  | [optional] 
**stable** | **bool** |  | [optional] 
**candidate** | **bool** |  | [optional] 
**available** | **bool** |  | [optional] 
**marked_for_deletion** | **bool** |  | [optional] 
**sortable_version** | **str** |  | [optional] 
**accounts_count** | **int** |  | [optional] 

## Example

```python
from qu.crm.models.product_version import ProductVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ProductVersion from a JSON string
product_version_instance = ProductVersion.from_json(json)
# print the JSON string representation of the object
print ProductVersion.to_json()

# convert the object into a dict
product_version_dict = product_version_instance.to_dict()
# create an instance of ProductVersion from a dict
product_version_form_dict = product_version.from_dict(product_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


