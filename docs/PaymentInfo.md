# PaymentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** |  | 
**detail** | **str** |  | [optional] 
**card_expire** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.payment_info import PaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInfo from a JSON string
payment_info_instance = PaymentInfo.from_json(json)
# print the JSON string representation of the object
print PaymentInfo.to_json()

# convert the object into a dict
payment_info_dict = payment_info_instance.to_dict()
# create an instance of PaymentInfo from a dict
payment_info_form_dict = payment_info.from_dict(payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


