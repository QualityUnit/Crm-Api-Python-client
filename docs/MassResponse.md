# MassResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_ids** | **List[str]** |  | [optional] 
**error_ids** | **List[str]** |  | [optional] 

## Example

```python
from qu.crm.models.mass_response import MassResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MassResponse from a JSON string
mass_response_instance = MassResponse.from_json(json)
# print the JSON string representation of the object
print MassResponse.to_json()

# convert the object into a dict
mass_response_dict = mass_response_instance.to_dict()
# create an instance of MassResponse from a dict
mass_response_form_dict = mass_response.from_dict(mass_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


