# DiscountValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**value_type** | **str** |  | [optional] [readonly] 
**value** | **int** |  | [optional] [readonly] 

## Example

```python
from qu.crm.models.discount_value import DiscountValue

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountValue from a JSON string
discount_value_instance = DiscountValue.from_json(json)
# print the JSON string representation of the object
print DiscountValue.to_json()

# convert the object into a dict
discount_value_dict = discount_value_instance.to_dict()
# create an instance of DiscountValue from a dict
discount_value_form_dict = discount_value.from_dict(discount_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


