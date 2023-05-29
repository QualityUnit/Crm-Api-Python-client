# SummaryInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**paid_at** | **datetime** |  | [optional] 
**price_billed** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.summary_invoice import SummaryInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryInvoice from a JSON string
summary_invoice_instance = SummaryInvoice.from_json(json)
# print the JSON string representation of the object
print SummaryInvoice.to_json()

# convert the object into a dict
summary_invoice_dict = summary_invoice_instance.to_dict()
# create an instance of SummaryInvoice from a dict
summary_invoice_form_dict = summary_invoice.from_dict(summary_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


