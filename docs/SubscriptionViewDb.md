# SubscriptionViewDb


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**var_pass** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.subscription_view_db import SubscriptionViewDb

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionViewDb from a JSON string
subscription_view_db_instance = SubscriptionViewDb.from_json(json)
# print the JSON string representation of the object
print SubscriptionViewDb.to_json()

# convert the object into a dict
subscription_view_db_dict = subscription_view_db_instance.to_dict()
# create an instance of SubscriptionViewDb from a dict
subscription_view_db_form_dict = subscription_view_db.from_dict(subscription_view_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


