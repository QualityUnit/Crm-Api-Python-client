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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from qu.crm.models.la_kb_parked import LaKbParked

class LaKbDomain(BaseModel):
    """
    LaKbDomain
    """
    domain: StrictStr = Field(...)
    ssl_crt: StrictStr = Field(...)
    ssl_key: StrictStr = Field(...)
    kbs: conlist(LaKbParked) = Field(..., description="knowledgebases parked on this domain")
    __properties = ["domain", "ssl_crt", "ssl_key", "kbs"]

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
    def from_json(cls, json_str: str) -> LaKbDomain:
        """Create an instance of LaKbDomain from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in kbs (list)
        _items = []
        if self.kbs:
            for _item in self.kbs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['kbs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LaKbDomain:
        """Create an instance of LaKbDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LaKbDomain.parse_obj(obj)

        _obj = LaKbDomain.parse_obj({
            "domain": obj.get("domain"),
            "ssl_crt": obj.get("ssl_crt"),
            "ssl_key": obj.get("ssl_key"),
            "kbs": [LaKbParked.from_dict(_item) for _item in obj.get("kbs")] if obj.get("kbs") is not None else None
        })
        return _obj

