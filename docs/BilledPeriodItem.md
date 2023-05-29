# BilledPeriodItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | F - forward fee, LF - last forward fee, U - usage, D - discount, O - overpayment, LO - last overpayment | 
**price** | **float** |  | 
**description** | **str** |  | 
**from_date** | **datetime** |  | 
**to_date** | **datetime** |  | 

## Example

```python
from qu.crm.models.billed_period_item import BilledPeriodItem

# TODO update the JSON string below
json = "{}"
# create an instance of BilledPeriodItem from a JSON string
billed_period_item_instance = BilledPeriodItem.from_json(json)
# print the JSON string representation of the object
print BilledPeriodItem.to_json()

# convert the object into a dict
billed_period_item_dict = billed_period_item_instance.to_dict()
# create an instance of BilledPeriodItem from a dict
billed_period_item_form_dict = billed_period_item.from_dict(billed_period_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


