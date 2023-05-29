# CustomDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_domain** | **str** |  | [optional] 
**ssl_key** | **str** |  | [optional] 
**ssl_crt** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.custom_domain import CustomDomain

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDomain from a JSON string
custom_domain_instance = CustomDomain.from_json(json)
# print the JSON string representation of the object
print CustomDomain.to_json()

# convert the object into a dict
custom_domain_dict = custom_domain_instance.to_dict()
# create an instance of CustomDomain from a dict
custom_domain_form_dict = custom_domain.from_dict(custom_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


