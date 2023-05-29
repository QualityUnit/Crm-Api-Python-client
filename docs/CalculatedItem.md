# CalculatedItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**count** | **float** |  | [optional] 
**description** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from qu.crm.models.calculated_item import CalculatedItem

# TODO update the JSON string below
json = "{}"
# create an instance of CalculatedItem from a JSON string
calculated_item_instance = CalculatedItem.from_json(json)
# print the JSON string representation of the object
print CalculatedItem.to_json()

# convert the object into a dict
calculated_item_dict = calculated_item_instance.to_dict()
# create an instance of CalculatedItem from a dict
calculated_item_form_dict = calculated_item.from_dict(calculated_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


