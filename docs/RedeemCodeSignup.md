# RedeemCodeSignup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**subdomain** | **str** |  | 
**grtoken** | **str** |  | 
**source_id** | **str** |  | [optional] 
**pap_visitor_id** | **str** |  | [optional] 
**ga_client_id** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.redeem_code_signup import RedeemCodeSignup

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemCodeSignup from a JSON string
redeem_code_signup_instance = RedeemCodeSignup.from_json(json)
# print the JSON string representation of the object
print RedeemCodeSignup.to_json()

# convert the object into a dict
redeem_code_signup_dict = redeem_code_signup_instance.to_dict()
# create an instance of RedeemCodeSignup from a dict
redeem_code_signup_form_dict = redeem_code_signup.from_dict(redeem_code_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


