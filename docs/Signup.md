# Signup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_id** | **str** |  | 
**subdomain** | **str** |  | 
**language** | **str** |  | [optional] 
**initial_api_key** | **str** |  | [optional] 
**billing_period** | **str** |  | [optional] [default to '1m']
**note** | **str** |  | [optional] 
**addons** | **List[str]** |  | [optional] 
**source_id** | **str** |  | [optional] 
**grtoken** | **str** |  | [optional] 
**pap_visitor_id** | **str** |  | [optional] 
**ga_client_id** | **str** |  | [optional] 
**promo** | **bool** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from qu.crm.models.signup import Signup

# TODO update the JSON string below
json = "{}"
# create an instance of Signup from a JSON string
signup_instance = Signup.from_json(json)
# print the JSON string representation of the object
print Signup.to_json()

# convert the object into a dict
signup_dict = signup_instance.to_dict()
# create an instance of Signup from a dict
signup_form_dict = signup.from_dict(signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


