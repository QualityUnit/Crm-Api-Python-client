# IndexStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**index_count** | **str** |  | [optional] 
**date_changed** | **datetime** |  | [optional] 

## Example

```python
from qu.crm.models.index_status import IndexStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IndexStatus from a JSON string
index_status_instance = IndexStatus.from_json(json)
# print the JSON string representation of the object
print IndexStatus.to_json()

# convert the object into a dict
index_status_dict = index_status_instance.to_dict()
# create an instance of IndexStatus from a dict
index_status_form_dict = index_status.from_dict(index_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


