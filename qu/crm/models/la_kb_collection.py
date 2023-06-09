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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from qu.crm.models.la_kb_domain import LaKbDomain
from qu.crm.models.la_kb_proxy import LaKbProxy

class LaKbCollection(BaseModel):
    """
    LaKbCollection
    """
    parked: Optional[conlist(LaKbDomain)] = Field(None, description="domains of parked knowledgebases")
    proxy: Optional[conlist(LaKbProxy)] = Field(None, description="proxied knowledgebases")
    __properties = ["parked", "proxy"]

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
    def from_json(cls, json_str: str) -> LaKbCollection:
        """Create an instance of LaKbCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in parked (list)
        _items = []
        if self.parked:
            for _item in self.parked:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parked'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in proxy (list)
        _items = []
        if self.proxy:
            for _item in self.proxy:
                if _item:
                    _items.append(_item.to_dict())
            _dict['proxy'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LaKbCollection:
        """Create an instance of LaKbCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LaKbCollection.parse_obj(obj)

        _obj = LaKbCollection.parse_obj({
            "parked": [LaKbDomain.from_dict(_item) for _item in obj.get("parked")] if obj.get("parked") is not None else None,
            "proxy": [LaKbProxy.from_dict(_item) for _item in obj.get("proxy")] if obj.get("proxy") is not None else None
        })
        return _obj

