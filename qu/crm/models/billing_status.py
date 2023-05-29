# coding: utf-8

"""
    CRM API

    This page contains complete API documentation for CRM software.  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: support@qualityunit.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class BillingStatus(BaseModel):
    """
    BillingStatus
    """
    status: Optional[StrictStr] = Field(None, description="N - No billing A - Billing active S = Billing stopped ")
    valid_to_date: Optional[datetime] = Field(None, description="Date and time of automatic suspension of subscription if there is not successful payment until then.")
    next_billing_date: Optional[datetime] = Field(None, description="Next scheduled billing date.")
    billing_day: Optional[StrictInt] = Field(None, description="Start day of the next billing period.")
    billing_period: Optional[StrictStr] = Field(None, description="Current billing period.")
    billing_period_start: Optional[date] = Field(None, description="Date of the beginning of the current billing period")
    billing_period_end: Optional[date] = Field(None, description="Date of the end of the current billing period")
    errors: Optional[StrictInt] = Field(None, description="Number of charge errors since last successful billing or account unsuspend.")
    last_error_date: Optional[datetime] = Field(None, description="Time an date of the last failed charge attempt. Only present if number or errors is greater than 0.")
    payment_compatible: Optional[StrictBool] = Field(None, description="True if used payment method is fully compatible with selected country, false otherwise. False when either payment method or country is not set.")
    uses_legacy_billing: Optional[StrictBool] = None
    __properties = ["status", "valid_to_date", "next_billing_date", "billing_day", "billing_period", "billing_period_start", "billing_period_end", "errors", "last_error_date", "payment_compatible", "uses_legacy_billing"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('N', 'A', 'S'):
            raise ValueError("must be one of enum values ('N', 'A', 'S')")
        return value

    @validator('billing_period')
    def billing_period_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('1m', '1y'):
            raise ValueError("must be one of enum values ('1m', '1y')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BillingStatus:
        """Create an instance of BillingStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BillingStatus:
        """Create an instance of BillingStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BillingStatus.parse_obj(obj)

        _obj = BillingStatus.parse_obj({
            "status": obj.get("status"),
            "valid_to_date": obj.get("valid_to_date"),
            "next_billing_date": obj.get("next_billing_date"),
            "billing_day": obj.get("billing_day"),
            "billing_period": obj.get("billing_period"),
            "billing_period_start": obj.get("billing_period_start"),
            "billing_period_end": obj.get("billing_period_end"),
            "errors": obj.get("errors"),
            "last_error_date": obj.get("last_error_date"),
            "payment_compatible": obj.get("payment_compatible"),
            "uses_legacy_billing": obj.get("uses_legacy_billing")
        })
        return _obj
