# SubscriptionViewData

additional subscription data shown by admin interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[Addon]**](Addon.md) |  | [optional] 
**billing_status** | [**BillingStatus**](BillingStatus.md) |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**domain** | [**Domain**](Domain.md) |  | [optional] 
**note** | [**Note**](Note.md) |  | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**variation_addons** | [**List[Addon]**](Addon.md) |  | [optional] 
**account_manager** | [**AccountManager**](AccountManager.md) |  | [optional] 
**db** | [**SubscriptionViewDb**](SubscriptionViewDb.md) |  | [optional] 
**version_info** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**locks** | **List[str]** |  | [optional] 
**initial_login_attempts** | [**InitialLoginAttempts**](InitialLoginAttempts.md) |  | [optional] 
**initial_lang** | [**InitialLang**](InitialLang.md) |  | [optional] 
**public_ip** | [**PublicIp**](PublicIp.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**owner_email** | [**OwnerEmail**](OwnerEmail.md) |  | [optional] 
**asterisk_host** | [**AsteriskHost**](AsteriskHost.md) |  | [optional] 
**aws_region** | [**AwsRegion**](AwsRegion.md) |  | [optional] 
**track_ga_client** | [**TrackGaClient**](TrackGaClient.md) |  | [optional] 
**track_pap_signup_ip** | [**TrackPapSignupIp**](TrackPapSignupIp.md) |  | [optional] 
**track_pap_user_agent** | [**TrackPapUserAgent**](TrackPapUserAgent.md) |  | [optional] 
**hosted_api_key** | [**HostedApiKey**](HostedApiKey.md) |  | [optional] 

## Example

```python
from qu.crm.models.subscription_view_data import SubscriptionViewData

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionViewData from a JSON string
subscription_view_data_instance = SubscriptionViewData.from_json(json)
# print the JSON string representation of the object
print SubscriptionViewData.to_json()

# convert the object into a dict
subscription_view_data_dict = subscription_view_data_instance.to_dict()
# create an instance of SubscriptionViewData from a dict
subscription_view_data_form_dict = subscription_view_data.from_dict(subscription_view_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


