# HackDummyPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**subscription_id** | **str** |  | 

## Example

```python
from qu.crm.models.hack_dummy_payment import HackDummyPayment

# TODO update the JSON string below
json = "{}"
# create an instance of HackDummyPayment from a JSON string
hack_dummy_payment_instance = HackDummyPayment.from_json(json)
# print the JSON string representation of the object
print HackDummyPayment.to_json()

# convert the object into a dict
hack_dummy_payment_dict = hack_dummy_payment_instance.to_dict()
# create an instance of HackDummyPayment from a dict
hack_dummy_payment_form_dict = hack_dummy_payment.from_dict(hack_dummy_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


