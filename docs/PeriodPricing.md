# PeriodPricing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**metrics** | [**List[BillingMetric]**](BillingMetric.md) |  | [optional] 
**base_price** | **int** |  | [optional] 

## Example

```python
from qu.crm.models.period_pricing import PeriodPricing

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodPricing from a JSON string
period_pricing_instance = PeriodPricing.from_json(json)
# print the JSON string representation of the object
print PeriodPricing.to_json()

# convert the object into a dict
period_pricing_dict = period_pricing_instance.to_dict()
# create an instance of PeriodPricing from a dict
period_pricing_form_dict = period_pricing.from_dict(period_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


