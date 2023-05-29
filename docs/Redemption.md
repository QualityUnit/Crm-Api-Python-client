# Redemption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeemer_name** | **str** |  | [readonly] 
**redeemer_email** | **str** |  | [readonly] 
**redeemed_at** | **str** |  | [readonly] 
**subscription_id** | **str** |  | [optional] [readonly] 

## Example

```python
from qu.crm.models.redemption import Redemption

# TODO update the JSON string below
json = "{}"
# create an instance of Redemption from a JSON string
redemption_instance = Redemption.from_json(json)
# print the JSON string representation of the object
print Redemption.to_json()

# convert the object into a dict
redemption_dict = redemption_instance.to_dict()
# create an instance of Redemption from a dict
redemption_form_dict = redemption.from_dict(redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


