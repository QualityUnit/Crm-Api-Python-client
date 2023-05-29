# InvoiceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 

## Example

```python
from qu.crm.models.invoice_item import InvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItem from a JSON string
invoice_item_instance = InvoiceItem.from_json(json)
# print the JSON string representation of the object
print InvoiceItem.to_json()

# convert the object into a dict
invoice_item_dict = invoice_item_instance.to_dict()
# create an instance of InvoiceItem from a dict
invoice_item_form_dict = invoice_item.from_dict(invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


