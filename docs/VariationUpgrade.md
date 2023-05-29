# VariationUpgrade


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation** | [**Variation**](Variation.md) |  | [optional] 
**addons** | [**List[Addon]**](Addon.md) |  | [optional] 
**billing_periods** | [**List[PeriodPricing]**](PeriodPricing.md) |  | [optional] 
**metrics** | [**List[BillingMetric]**](BillingMetric.md) |  | [optional] 
**base_price** | **int** |  | [optional] 
**discounts** | [**List[DiscountValue]**](DiscountValue.md) |  | [optional] 

## Example

```python
from qu.crm.models.variation_upgrade import VariationUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of VariationUpgrade from a JSON string
variation_upgrade_instance = VariationUpgrade.from_json(json)
# print the JSON string representation of the object
print VariationUpgrade.to_json()

# convert the object into a dict
variation_upgrade_dict = variation_upgrade_instance.to_dict()
# create an instance of VariationUpgrade from a dict
variation_upgrade_form_dict = variation_upgrade.from_dict(variation_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


