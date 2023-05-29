# FailedPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**origin** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**processor_id** | **str** |  | [optional] 
**processor_response** | **str** |  | [optional] 
**attempt_number** | **int** |  | [optional] 

## Example

```python
from qu.crm.models.failed_payment import FailedPayment

# TODO update the JSON string below
json = "{}"
# create an instance of FailedPayment from a JSON string
failed_payment_instance = FailedPayment.from_json(json)
# print the JSON string representation of the object
print FailedPayment.to_json()

# convert the object into a dict
failed_payment_dict = failed_payment_instance.to_dict()
# create an instance of FailedPayment from a dict
failed_payment_form_dict = failed_payment.from_dict(failed_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


