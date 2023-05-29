# AccountStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**today_new** | **float** |  | [optional] 
**today_new_paid** | **float** |  | [optional] 
**active** | **float** |  | [optional] 
**active_paid** | **float** |  | [optional] 
**agents** | **float** |  | [optional] 
**agents_paid** | **float** |  | [optional] 
**variations_active** | **object** | active variations | [optional] 
**variations_agents** | **object** | agents per variation | [optional] 

## Example

```python
from qu.crm.models.account_stats import AccountStats

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStats from a JSON string
account_stats_instance = AccountStats.from_json(json)
# print the JSON string representation of the object
print AccountStats.to_json()

# convert the object into a dict
account_stats_dict = account_stats_instance.to_dict()
# create an instance of AccountStats from a dict
account_stats_form_dict = account_stats.from_dict(account_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


