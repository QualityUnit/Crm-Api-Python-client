# ReindexStatusData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastic_active** | **bool** |  | [optional] 
**index_status** | [**List[IndexStatus]**](IndexStatus.md) |  | [optional] 

## Example

```python
from qu.crm.models.reindex_status_data import ReindexStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of ReindexStatusData from a JSON string
reindex_status_data_instance = ReindexStatusData.from_json(json)
# print the JSON string representation of the object
print ReindexStatusData.to_json()

# convert the object into a dict
reindex_status_data_dict = reindex_status_data_instance.to_dict()
# create an instance of ReindexStatusData from a dict
reindex_status_data_form_dict = reindex_status_data.from_dict(reindex_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


