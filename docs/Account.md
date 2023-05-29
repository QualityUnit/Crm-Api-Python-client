# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**cluster_id** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**custom_domain** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**status** | **str** | I - installing A - active S - suspended T - terminated D - deleted  | [optional] 

## Example

```python
from qu.crm.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print Account.to_json()

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


