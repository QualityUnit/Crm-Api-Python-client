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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class InvoiceItem(BaseModel):
    """
    InvoiceItem
    """
    type: Optional[StrictStr] = None
    price: Optional[Union[StrictFloat, StrictInt]] = None
    description: Optional[StrictStr] = None
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
    __properties = ["type", "price", "description", "from_date", "to_date"]

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
    def from_json(cls, json_str: str) -> InvoiceItem:
        """Create an instance of InvoiceItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InvoiceItem:
        """Create an instance of InvoiceItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InvoiceItem.parse_obj(obj)

        _obj = InvoiceItem.parse_obj({
            "type": obj.get("type"),
            "price": obj.get("price"),
            "description": obj.get("description"),
            "from_date": obj.get("from_date"),
            "to_date": obj.get("to_date")
        })
        return _obj

