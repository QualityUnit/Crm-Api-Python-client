# BillingStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | N - No billing A - Billing active S &#x3D; Billing stopped  | [optional] 
**valid_to_date** | **datetime** | Date and time of automatic suspension of subscription if there is not successful payment until then. | [optional] 
**next_billing_date** | **datetime** | Next scheduled billing date. | [optional] 
**billing_day** | **int** | Start day of the next billing period. | [optional] 
**billing_period** | **str** | Current billing period. | [optional] 
**billing_period_start** | **date** | Date of the beginning of the current billing period | [optional] 
**billing_period_end** | **date** | Date of the end of the current billing period | [optional] 
**errors** | **int** | Number of charge errors since last successful billing or account unsuspend. | [optional] 
**last_error_date** | **datetime** | Time an date of the last failed charge attempt. Only present if number or errors is greater than 0. | [optional] 
**payment_compatible** | **bool** | True if used payment method is fully compatible with selected country, false otherwise. False when either payment method or country is not set. | [optional] 
**uses_legacy_billing** | **bool** |  | [optional] 

## Example

```python
from qu.crm.models.billing_status import BillingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BillingStatus from a JSON string
billing_status_instance = BillingStatus.from_json(json)
# print the JSON string representation of the object
print BillingStatus.to_json()

# convert the object into a dict
billing_status_dict = billing_status_instance.to_dict()
# create an instance of BillingStatus from a dict
billing_status_form_dict = billing_status.from_dict(billing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


