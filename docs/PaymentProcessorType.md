# PaymentProcessorType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processor_type** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**init_token** | **str** |  | [optional] 
**braintree_merchant_account_id** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.payment_processor_type import PaymentProcessorType

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentProcessorType from a JSON string
payment_processor_type_instance = PaymentProcessorType.from_json(json)
# print the JSON string representation of the object
print PaymentProcessorType.to_json()

# convert the object into a dict
payment_processor_type_dict = payment_processor_type_instance.to_dict()
# create an instance of PaymentProcessorType from a dict
payment_processor_type_form_dict = payment_processor_type.from_dict(payment_processor_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


