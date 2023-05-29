# Invoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**refund_id** | **str** |  | [optional] 
**created_date** | **datetime** | Invoice issued date | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**paid_date** | **datetime** |  | [optional] 
**price** | **float** |  | [optional] 
**price_billed** | **float** |  | [optional] 
**vat_rate** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**items** | [**List[InvoiceItem]**](InvoiceItem.md) |  | [optional] 

## Example

```python
from qu.crm.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print Invoice.to_json()

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_form_dict = invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


