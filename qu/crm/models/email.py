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


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr, validator

class Email(BaseModel):
    """
    Email
    """
    id: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    date_created: Optional[StrictStr] = None
    date_delivered: Optional[StrictStr] = None
    from_mail: Optional[StrictStr] = None
    subject: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    recipients: Optional[StrictStr] = None
    cc_recipients: Optional[StrictStr] = None
    bcc_recipients: Optional[StrictStr] = None
    extra_headers: Optional[StrictStr] = None
    retries: Optional[StrictStr] = None
    last_retry: Optional[StrictStr] = None
    error: Optional[StrictStr] = None
    __properties = ["id", "status", "date_created", "date_delivered", "from_mail", "subject", "body", "recipients", "cc_recipients", "bcc_recipients", "extra_headers", "retries", "last_retry", "error"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('C', 'F', 'P', 'S', 'D'):
            raise ValueError("must be one of enum values ('C', 'F', 'P', 'S', 'D')")
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
    def from_json(cls, json_str: str) -> Email:
        """Create an instance of Email from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Email:
        """Create an instance of Email from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Email.parse_obj(obj)

        _obj = Email.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "date_created": obj.get("date_created"),
            "date_delivered": obj.get("date_delivered"),
            "from_mail": obj.get("from_mail"),
            "subject": obj.get("subject"),
            "body": obj.get("body"),
            "recipients": obj.get("recipients"),
            "cc_recipients": obj.get("cc_recipients"),
            "bcc_recipients": obj.get("bcc_recipients"),
            "extra_headers": obj.get("extra_headers"),
            "retries": obj.get("retries"),
            "last_retry": obj.get("last_retry"),
            "error": obj.get("error")
        })
        return _obj

