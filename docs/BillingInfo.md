# BillingInfo

inherits all fields from Customer definition, and adds 'force' field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** |  | [optional] [default to False]
**name** | **str** |  | 
**email** | **str** |  | 
**company** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**city** | **str** |  | 
**state** | **str** |  | [optional] 
**country** | **str** |  | 
**zip** | **str** |  | 
**vat_id** | **str** |  | [optional] 
**ico_sk** | **str** |  | [optional] 
**dic_sk** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.billing_info import BillingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInfo from a JSON string
billing_info_instance = BillingInfo.from_json(json)
# print the JSON string representation of the object
print BillingInfo.to_json()

# convert the object into a dict
billing_info_dict = billing_info_instance.to_dict()
# create an instance of BillingInfo from a dict
billing_info_form_dict = billing_info.from_dict(billing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


