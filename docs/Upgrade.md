# Upgrade


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_id** | **str** |  | 
**addons** | **List[str]** |  | [optional] 
**billing_period** | **str** |  | [optional] [default to '1m']
**coupon** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.upgrade import Upgrade

# TODO update the JSON string below
json = "{}"
# create an instance of Upgrade from a JSON string
upgrade_instance = Upgrade.from_json(json)
# print the JSON string representation of the object
print Upgrade.to_json()

# convert the object into a dict
upgrade_dict = upgrade_instance.to_dict()
# create an instance of Upgrade from a dict
upgrade_form_dict = upgrade.from_dict(upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


