# ResellerUpgrade


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_id** | **str** |  | 
**addons** | **List[str]** |  | [optional] 

## Example

```python
from qu.crm.models.reseller_upgrade import ResellerUpgrade

# TODO update the JSON string below
json = "{}"
# create an instance of ResellerUpgrade from a JSON string
reseller_upgrade_instance = ResellerUpgrade.from_json(json)
# print the JSON string representation of the object
print ResellerUpgrade.to_json()

# convert the object into a dict
reseller_upgrade_dict = reseller_upgrade_instance.to_dict()
# create an instance of ResellerUpgrade from a dict
reseller_upgrade_form_dict = reseller_upgrade.from_dict(reseller_upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


