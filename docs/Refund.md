# Refund


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**is_full_refund** | **bool** |  | [optional] 
**refunded_by** | **str** |  | [optional] 
**refunded_date** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.refund import Refund

# TODO update the JSON string below
json = "{}"
# create an instance of Refund from a JSON string
refund_instance = Refund.from_json(json)
# print the JSON string representation of the object
print Refund.to_json()

# convert the object into a dict
refund_dict = refund_instance.to_dict()
# create an instance of Refund from a dict
refund_form_dict = refund.from_dict(refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


