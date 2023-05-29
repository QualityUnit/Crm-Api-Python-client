# ResellerSignup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_id** | **str** |  | 
**subdomain** | **str** |  | 
**initial_name** | **str** | The name of initial application user | 
**initial_email** | **str** | The email of initial application user | 
**initial_pass** | **str** | Password of initial application user | [optional] 
**initial_language** | **str** | Code of initial application language | [optional] 
**initial_api_key** | **str** | The initial application api key | [optional] 

## Example

```python
from qu.crm.models.reseller_signup import ResellerSignup

# TODO update the JSON string below
json = "{}"
# create an instance of ResellerSignup from a JSON string
reseller_signup_instance = ResellerSignup.from_json(json)
# print the JSON string representation of the object
print ResellerSignup.to_json()

# convert the object into a dict
reseller_signup_dict = reseller_signup_instance.to_dict()
# create an instance of ResellerSignup from a dict
reseller_signup_form_dict = reseller_signup.from_dict(reseller_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


