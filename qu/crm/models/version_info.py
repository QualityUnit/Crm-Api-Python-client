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



from pydantic import BaseModel, Field, StrictBool, StrictStr

class VersionInfo(BaseModel):
    """
    VersionInfo
    """
    latest_stable: StrictStr = Field(...)
    latest_available: StrictStr = Field(...)
    latest_candidate: StrictStr = Field(...)
    is_available: StrictBool = Field(...)
    is_stable: StrictBool = Field(...)
    is_candidate: StrictBool = Field(...)
    __properties = ["latest_stable", "latest_available", "latest_candidate", "is_available", "is_stable", "is_candidate"]

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
    def from_json(cls, json_str: str) -> VersionInfo:
        """Create an instance of VersionInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VersionInfo:
        """Create an instance of VersionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VersionInfo.parse_obj(obj)

        _obj = VersionInfo.parse_obj({
            "latest_stable": obj.get("latest_stable"),
            "latest_available": obj.get("latest_available"),
            "latest_candidate": obj.get("latest_candidate"),
            "is_available": obj.get("is_available"),
            "is_stable": obj.get("is_stable"),
            "is_candidate": obj.get("is_candidate")
        })
        return _obj
