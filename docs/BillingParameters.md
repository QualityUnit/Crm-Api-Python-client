# BillingParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_period** | **str** |  | [optional] 
**variation_id** | **str** |  | [optional] 
**addons** | **List[str]** | addon codenames | [optional] 
**coupon** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.billing_parameters import BillingParameters

# TODO update the JSON string below
json = "{}"
# create an instance of BillingParameters from a JSON string
billing_parameters_instance = BillingParameters.from_json(json)
# print the JSON string representation of the object
print BillingParameters.to_json()

# convert the object into a dict
billing_parameters_dict = billing_parameters_instance.to_dict()
# create an instance of BillingParameters from a dict
billing_parameters_form_dict = billing_parameters.from_dict(billing_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


