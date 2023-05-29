# Email


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_delivered** | **str** |  | [optional] 
**from_mail** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**recipients** | **str** |  | [optional] 
**cc_recipients** | **str** |  | [optional] 
**bcc_recipients** | **str** |  | [optional] 
**extra_headers** | **str** |  | [optional] 
**retries** | **str** |  | [optional] 
**last_retry** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from qu.crm.models.email import Email

# TODO update the JSON string below
json = "{}"
# create an instance of Email from a JSON string
email_instance = Email.from_json(json)
# print the JSON string representation of the object
print Email.to_json()

# convert the object into a dict
email_dict = email_instance.to_dict()
# create an instance of Email from a dict
email_form_dict = email.from_dict(email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


