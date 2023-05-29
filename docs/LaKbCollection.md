# LaKbCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parked** | [**List[LaKbDomain]**](LaKbDomain.md) | domains of parked knowledgebases | [optional] 
**proxy** | [**List[LaKbProxy]**](LaKbProxy.md) | proxied knowledgebases | [optional] 

## Example

```python
from qu.crm.models.la_kb_collection import LaKbCollection

# TODO update the JSON string below
json = "{}"
# create an instance of LaKbCollection from a JSON string
la_kb_collection_instance = LaKbCollection.from_json(json)
# print the JSON string representation of the object
print LaKbCollection.to_json()

# convert the object into a dict
la_kb_collection_dict = la_kb_collection_instance.to_dict()
# create an instance of LaKbCollection from a dict
la_kb_collection_form_dict = la_kb_collection.from_dict(la_kb_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


