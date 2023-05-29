# SubscriptionStatusHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | I - Installing A - Active S - Suspended T - Terminated D - Deleted  | [optional] 
**date_of_status** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.subscription_status_history import SubscriptionStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionStatusHistory from a JSON string
subscription_status_history_instance = SubscriptionStatusHistory.from_json(json)
# print the JSON string representation of the object
print SubscriptionStatusHistory.to_json()

# convert the object into a dict
subscription_status_history_dict = subscription_status_history_instance.to_dict()
# create an instance of SubscriptionStatusHistory from a dict
subscription_status_history_form_dict = subscription_status_history.from_dict(subscription_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


