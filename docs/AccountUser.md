# AccountUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**is_online** | **bool** |  | [optional] 

## Example

```python
from qu.crm.models.account_user import AccountUser

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUser from a JSON string
account_user_instance = AccountUser.from_json(json)
# print the JSON string representation of the object
print AccountUser.to_json()

# convert the object into a dict
account_user_dict = account_user_instance.to_dict()
# create an instance of AccountUser from a dict
account_user_form_dict = account_user.from_dict(account_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


