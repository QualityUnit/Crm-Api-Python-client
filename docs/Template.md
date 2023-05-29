# Template


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**recipient** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**variation_id** | **str** |  | [optional] 
**occasion** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**sender** | **str** |  | [optional] 
**bcc_recipients** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print Template.to_json()

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_form_dict = template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


