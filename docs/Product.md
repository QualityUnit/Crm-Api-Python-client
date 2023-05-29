# Product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**family** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**top_domain** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print Product.to_json()

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_form_dict = product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


