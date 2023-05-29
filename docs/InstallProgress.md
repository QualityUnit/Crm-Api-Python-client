# InstallProgress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_status** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**login_url** | **str** |  | [optional] 
**login_token** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.install_progress import InstallProgress

# TODO update the JSON string below
json = "{}"
# create an instance of InstallProgress from a JSON string
install_progress_instance = InstallProgress.from_json(json)
# print the JSON string representation of the object
print InstallProgress.to_json()

# convert the object into a dict
install_progress_dict = install_progress_instance.to_dict()
# create an instance of InstallProgress from a dict
install_progress_form_dict = install_progress.from_dict(install_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


