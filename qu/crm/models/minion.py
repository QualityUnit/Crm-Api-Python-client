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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class Minion(BaseModel):
    """
    Minion
    """
    id: StrictStr = Field(...)
    cluster: Optional[StrictStr] = None
    ip: Optional[StrictStr] = None
    created_date: Optional[datetime] = None
    up_date: Optional[datetime] = None
    down_date: Optional[datetime] = None
    goingup_date: Optional[datetime] = None
    roles: Optional[conlist(StrictStr)] = None
    __properties = ["id", "cluster", "ip", "created_date", "up_date", "down_date", "goingup_date", "roles"]

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
    def from_json(cls, json_str: str) -> Minion:
        """Create an instance of Minion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Minion:
        """Create an instance of Minion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Minion.parse_obj(obj)

        _obj = Minion.parse_obj({
            "id": obj.get("id"),
            "cluster": obj.get("cluster"),
            "ip": obj.get("ip"),
            "created_date": obj.get("created_date"),
            "up_date": obj.get("up_date"),
            "down_date": obj.get("down_date"),
            "goingup_date": obj.get("goingup_date"),
            "roles": obj.get("roles")
        })
        return _obj

