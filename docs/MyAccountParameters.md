# MyAccountParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_id** | **str** |  | [optional] 
**addons** | **str** |  | [optional] 
**agents_count** | **str** |  | [optional] 
**knowledgebase_count** | **str** |  | [optional] 
**entry_point** | **str** |  | 
**is_standalone** | **bool** |  | [optional] 

## Example

```python
from qu.crm.models.my_account_parameters import MyAccountParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MyAccountParameters from a JSON string
my_account_parameters_instance = MyAccountParameters.from_json(json)
# print the JSON string representation of the object
print MyAccountParameters.to_json()

# convert the object into a dict
my_account_parameters_dict = my_account_parameters_instance.to_dict()
# create an instance of MyAccountParameters from a dict
my_account_parameters_form_dict = my_account_parameters.from_dict(my_account_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


