# RedeemCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**variation_id** | **str** |  | 
**expires_at** | **str** |  | [optional] 
**discount_template** | [**DiscountTemplate**](DiscountTemplate.md) |  | [optional] 
**redemption** | [**Redemption**](Redemption.md) |  | [optional] 

## Example

```python
from qu.crm.models.redeem_code import RedeemCode

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemCode from a JSON string
redeem_code_instance = RedeemCode.from_json(json)
# print the JSON string representation of the object
print RedeemCode.to_json()

# convert the object into a dict
redeem_code_dict = redeem_code_instance.to_dict()
# create an instance of RedeemCode from a dict
redeem_code_form_dict = redeem_code.from_dict(redeem_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


