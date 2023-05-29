# RefundRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.refund_request import RefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequest from a JSON string
refund_request_instance = RefundRequest.from_json(json)
# print the JSON string representation of the object
print RefundRequest.to_json()

# convert the object into a dict
refund_request_dict = refund_request_instance.to_dict()
# create an instance of RefundRequest from a dict
refund_request_form_dict = refund_request.from_dict(refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


