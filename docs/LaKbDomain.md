# LaKbDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**ssl_crt** | **str** |  | 
**ssl_key** | **str** |  | 
**kbs** | [**List[LaKbParked]**](LaKbParked.md) | knowledgebases parked on this domain | 

## Example

```python
from qu.crm.models.la_kb_domain import LaKbDomain

# TODO update the JSON string below
json = "{}"
# create an instance of LaKbDomain from a JSON string
la_kb_domain_instance = LaKbDomain.from_json(json)
# print the JSON string representation of the object
print LaKbDomain.to_json()

# convert the object into a dict
la_kb_domain_dict = la_kb_domain_instance.to_dict()
# create an instance of LaKbDomain from a dict
la_kb_domain_form_dict = la_kb_domain.from_dict(la_kb_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


