# Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**company** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**vat_id** | **str** |  | [optional] 
**ico_sk** | **str** |  | [optional] 
**dic_sk** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print Customer.to_json()

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_form_dict = customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


