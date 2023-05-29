# ReindexData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Reindex type: { contacts, tickets, knowledgebase, all } | 
**truncate** | **bool** |  | [optional] 
**include_date** | **bool** |  | [optional] 
**date_from** | **datetime** |  | [optional] 
**date_to** | **datetime** |  | [optional] 

## Example

```python
from qu.crm.models.reindex_data import ReindexData

# TODO update the JSON string below
json = "{}"
# create an instance of ReindexData from a JSON string
reindex_data_instance = ReindexData.from_json(json)
# print the JSON string representation of the object
print ReindexData.to_json()

# convert the object into a dict
reindex_data_dict = reindex_data_instance.to_dict()
# create an instance of ReindexData from a dict
reindex_data_form_dict = reindex_data.from_dict(reindex_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


