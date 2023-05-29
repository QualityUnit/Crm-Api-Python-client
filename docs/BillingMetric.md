# BillingMetric


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**amount_in_price** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**unit_size** | **int** |  | [optional] 

## Example

```python
from qu.crm.models.billing_metric import BillingMetric

# TODO update the JSON string below
json = "{}"
# create an instance of BillingMetric from a JSON string
billing_metric_instance = BillingMetric.from_json(json)
# print the JSON string representation of the object
print BillingMetric.to_json()

# convert the object into a dict
billing_metric_dict = billing_metric_instance.to_dict()
# create an instance of BillingMetric from a dict
billing_metric_form_dict = billing_metric.from_dict(billing_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


