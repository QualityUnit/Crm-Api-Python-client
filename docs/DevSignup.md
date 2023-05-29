# DevSignup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_id** | **str** |  | 
**subdomain** | **str** |  | 
**language** | **str** | Code of application language | [optional] 
**initial_api_key** | **str** | The initial application api key | [optional] 
**initial_pass** | **str** | Password of initial application user | [optional] 
**cluster** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | 

## Example

```python
from qu.crm.models.dev_signup import DevSignup

# TODO update the JSON string below
json = "{}"
# create an instance of DevSignup from a JSON string
dev_signup_instance = DevSignup.from_json(json)
# print the JSON string representation of the object
print DevSignup.to_json()

# convert the object into a dict
dev_signup_dict = dev_signup_instance.to_dict()
# create an instance of DevSignup from a dict
dev_signup_form_dict = dev_signup.from_dict(dev_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


