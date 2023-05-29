# Subscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**domain** | **str** | Default domain assigned to subscription when created (e.g. example.ladesk.com) | [optional] 
**custom_domain** | **str** | Additional domain parked to this subscription (e.g. support.example.com) | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_validity** | **datetime** |  | [optional] 
**status** | **str** | I - installing A - active S - suspended T - terminated D - deleted  | [optional] 
**account_id** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**is_latest** | **bool** |  | [optional] 
**update_policy** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**variation_id** | **str** |  | [optional] 
**usage** | **object** |  | [optional] 

## Example

```python
from qu.crm.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print Subscription.to_json()

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_form_dict = subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


