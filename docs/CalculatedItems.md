# CalculatedItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CalculatedItem]**](CalculatedItem.md) |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from qu.crm.models.calculated_items import CalculatedItems

# TODO update the JSON string below
json = "{}"
# create an instance of CalculatedItems from a JSON string
calculated_items_instance = CalculatedItems.from_json(json)
# print the JSON string representation of the object
print CalculatedItems.to_json()

# convert the object into a dict
calculated_items_dict = calculated_items_instance.to_dict()
# create an instance of CalculatedItems from a dict
calculated_items_form_dict = calculated_items.from_dict(calculated_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


