# PaymentErrorInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_instrument** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 

## Example

```python
from qu.crm.models.payment_error_info import PaymentErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentErrorInfo from a JSON string
payment_error_info_instance = PaymentErrorInfo.from_json(json)
# print the JSON string representation of the object
print PaymentErrorInfo.to_json()

# convert the object into a dict
payment_error_info_dict = payment_error_info_instance.to_dict()
# create an instance of PaymentErrorInfo from a dict
payment_error_info_form_dict = payment_error_info.from_dict(payment_error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


