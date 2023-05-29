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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class Addon(BaseModel):
    """
    presence of fields 'price' and 'active' depends on the context from which addon object is returned
    """
    codename: StrictStr = Field(...)
    name: StrictStr = Field(...)
    description: StrictStr = Field(...)
    state: StrictStr = Field(...)
    price: Optional[StrictInt] = None
    active: Optional[StrictBool] = None
    __properties = ["codename", "name", "description", "state", "price", "active"]

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
    def from_json(cls, json_str: str) -> Addon:
        """Create an instance of Addon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Addon:
        """Create an instance of Addon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Addon.parse_obj(obj)

        _obj = Addon.parse_obj({
            "codename": obj.get("codename"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "state": obj.get("state"),
            "price": obj.get("price"),
            "active": obj.get("active")
        })
        return _obj

