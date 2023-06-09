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

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr

class Refund(BaseModel):
    """
    Refund
    """
    id: Optional[StrictInt] = None
    invoice_number: Optional[StrictStr] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    is_full_refund: Optional[StrictBool] = None
    refunded_by: Optional[StrictStr] = None
    refunded_date: Optional[datetime] = None
    note: Optional[StrictStr] = None
    __properties = ["id", "invoice_number", "amount", "is_full_refund", "refunded_by", "refunded_date", "note"]

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
    def from_json(cls, json_str: str) -> Refund:
        """Create an instance of Refund from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Refund:
        """Create an instance of Refund from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Refund.parse_obj(obj)

        _obj = Refund.parse_obj({
            "id": obj.get("id"),
            "invoice_number": obj.get("invoice_number"),
            "amount": obj.get("amount"),
            "is_full_refund": obj.get("is_full_refund"),
            "refunded_by": obj.get("refunded_by"),
            "refunded_date": obj.get("refunded_date"),
            "note": obj.get("note")
        })
        return _obj

