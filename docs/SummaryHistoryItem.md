# SummaryHistoryItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_number** | **str** |  | [optional] 
**var_from** | **date** |  | [optional] 
**to** | **date** |  | [optional] 
**charged_invoices** | [**List[SummaryInvoice]**](SummaryInvoice.md) |  | [optional] 
**period** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 
**price_usd** | **float** |  | [optional] 

## Example

```python
from qu.crm.models.summary_history_item import SummaryHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryHistoryItem from a JSON string
summary_history_item_instance = SummaryHistoryItem.from_json(json)
# print the JSON string representation of the object
print SummaryHistoryItem.to_json()

# convert the object into a dict
summary_history_item_dict = summary_history_item_instance.to_dict()
# create an instance of SummaryHistoryItem from a dict
summary_history_item_form_dict = summary_history_item.from_dict(summary_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


