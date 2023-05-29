# ResellerSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**domain** | **str** | Default domain assigned to subscription when created (e.g. example.ladesk.com) | [optional] 
**custom_domain** | **str** | Additional domain parked to this subscription (e.g. support.example.com) | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_validity** | **datetime** |  | [optional] 
**status** | **str** | I - installing, A - active, S - suspended, T - terminated | [optional] 
**variation_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**initial_api_key** | **str** | The initial api key. Only included in signup response. | [optional] 
**initial_pass** | **str** | Password of initial application user. Only included in signup response. | [optional] 

## Example

```python
from qu.crm.models.reseller_subscription import ResellerSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ResellerSubscription from a JSON string
reseller_subscription_instance = ResellerSubscription.from_json(json)
# print the JSON string representation of the object
print ResellerSubscription.to_json()

# convert the object into a dict
reseller_subscription_dict = reseller_subscription_instance.to_dict()
# create an instance of ResellerSubscription from a dict
reseller_subscription_form_dict = reseller_subscription.from_dict(reseller_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


