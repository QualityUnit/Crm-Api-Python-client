# Variation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**billable** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**full_name** | **str** | Full name in format Product - Variation | [optional] 
**description** | **str** |  | [optional] 
**limits** | **object** |  | [optional] 

## Example

```python
from qu.crm.models.variation import Variation

# TODO update the JSON string below
json = "{}"
# create an instance of Variation from a JSON string
variation_instance = Variation.from_json(json)
# print the JSON string representation of the object
print Variation.to_json()

# convert the object into a dict
variation_dict = variation_instance.to_dict()
# create an instance of Variation from a dict
variation_form_dict = variation.from_dict(variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


