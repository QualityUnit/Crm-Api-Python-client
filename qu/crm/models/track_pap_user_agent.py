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
from pydantic import BaseModel, StrictStr

class TrackPapUserAgent(BaseModel):
    """
    TrackPapUserAgent
    """
    track_pap_user_agent: Optional[StrictStr] = None
    __properties = ["track_pap_user_agent"]

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
    def from_json(cls, json_str: str) -> TrackPapUserAgent:
        """Create an instance of TrackPapUserAgent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackPapUserAgent:
        """Create an instance of TrackPapUserAgent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackPapUserAgent.parse_obj(obj)

        _obj = TrackPapUserAgent.parse_obj({
            "track_pap_user_agent": obj.get("track_pap_user_agent")
        })
        return _obj

