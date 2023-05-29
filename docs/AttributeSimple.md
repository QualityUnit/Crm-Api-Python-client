# AttributeSimple


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.attribute_simple import AttributeSimple

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeSimple from a JSON string
attribute_simple_instance = AttributeSimple.from_json(json)
# print the JSON string representation of the object
print AttributeSimple.to_json()

# convert the object into a dict
attribute_simple_dict = attribute_simple_instance.to_dict()
# create an instance of AttributeSimple from a dict
attribute_simple_form_dict = attribute_simple.from_dict(attribute_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


