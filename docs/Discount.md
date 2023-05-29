# Discount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**subscription_id** | **str** |  | 
**name** | **str** |  | [optional] 
**type** | **str** |  | 
**value_type** | **str** |  | 
**value** | **int** |  | 
**note** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] [readonly] 
**date_created** | **str** |  | [optional] [readonly] 
**expiration_type** | **str** |  | [optional] 
**days_valid** | **str** |  | [optional] 
**ended_by** | **str** |  | [optional] [readonly] 
**date_ended** | **str** |  | [optional] [readonly] 

## Example

```python
from qu.crm.models.discount import Discount

# TODO update the JSON string below
json = "{}"
# create an instance of Discount from a JSON string
discount_instance = Discount.from_json(json)
# print the JSON string representation of the object
print Discount.to_json()

# convert the object into a dict
discount_dict = discount_instance.to_dict()
# create an instance of Discount from a dict
discount_form_dict = discount.from_dict(discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


