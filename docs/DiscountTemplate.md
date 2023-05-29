# DiscountTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value_type** | **str** |  | 
**value** | **int** |  | 
**days_valid** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.discount_template import DiscountTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountTemplate from a JSON string
discount_template_instance = DiscountTemplate.from_json(json)
# print the JSON string representation of the object
print DiscountTemplate.to_json()

# convert the object into a dict
discount_template_dict = discount_template_instance.to_dict()
# create an instance of DiscountTemplate from a dict
discount_template_form_dict = discount_template.from_dict(discount_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


