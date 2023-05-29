# BilledPeriod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** |  | 
**to_date** | **datetime** |  | 
**price** | **float** |  | 
**currency** | **str** |  | 
**items** | [**List[BilledPeriodItem]**](BilledPeriodItem.md) |  | 

## Example

```python
from qu.crm.models.billed_period import BilledPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of BilledPeriod from a JSON string
billed_period_instance = BilledPeriod.from_json(json)
# print the JSON string representation of the object
print BilledPeriod.to_json()

# convert the object into a dict
billed_period_dict = billed_period_instance.to_dict()
# create an instance of BilledPeriod from a dict
billed_period_form_dict = billed_period.from_dict(billed_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


