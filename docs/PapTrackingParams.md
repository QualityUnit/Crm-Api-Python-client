# PapTrackingParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_aid** | **str** |  | [optional] 
**a_bid** | **str** |  | [optional] 
**a_cid** | **str** |  | [optional] 
**a_rid** | **str** |  | [optional] 
**data1** | **str** |  | [optional] 
**data2** | **str** |  | [optional] 
**desturl** | **str** |  | [optional] 
**visit_processors** | **float** |  | [optional] 
**imp_processors** | **float** |  | [optional] 

## Example

```python
from qu.crm.models.pap_tracking_params import PapTrackingParams

# TODO update the JSON string below
json = "{}"
# create an instance of PapTrackingParams from a JSON string
pap_tracking_params_instance = PapTrackingParams.from_json(json)
# print the JSON string representation of the object
print PapTrackingParams.to_json()

# convert the object into a dict
pap_tracking_params_dict = pap_tracking_params_instance.to_dict()
# create an instance of PapTrackingParams from a dict
pap_tracking_params_form_dict = pap_tracking_params.from_dict(pap_tracking_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


