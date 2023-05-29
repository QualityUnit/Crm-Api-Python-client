# VariationUpgrades


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**VariationUpgrade**](VariationUpgrade.md) |  | [optional] 
**upgrades** | [**List[VariationUpgrade]**](VariationUpgrade.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**tax_per_cent** | **float** |  | [optional] 
**tax_included** | **bool** |  | [optional] 

## Example

```python
from qu.crm.models.variation_upgrades import VariationUpgrades

# TODO update the JSON string below
json = "{}"
# create an instance of VariationUpgrades from a JSON string
variation_upgrades_instance = VariationUpgrades.from_json(json)
# print the JSON string representation of the object
print VariationUpgrades.to_json()

# convert the object into a dict
variation_upgrades_dict = variation_upgrades_instance.to_dict()
# create an instance of VariationUpgrades from a dict
variation_upgrades_form_dict = variation_upgrades.from_dict(variation_upgrades_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


