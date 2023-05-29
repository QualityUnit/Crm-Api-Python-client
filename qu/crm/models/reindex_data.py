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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class ReindexData(BaseModel):
    """
    ReindexData
    """
    type: StrictStr = Field(..., description="Reindex type: { contacts, tickets, knowledgebase, all }")
    truncate: Optional[StrictBool] = None
    include_date: Optional[StrictBool] = Field(None, alias="includeDate")
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    __properties = ["type", "truncate", "includeDate", "date_from", "date_to"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('contacts', 'tickets', 'knowledgebase', 'all'):
            raise ValueError("must be one of enum values ('contacts', 'tickets', 'knowledgebase', 'all')")
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
    def from_json(cls, json_str: str) -> ReindexData:
        """Create an instance of ReindexData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReindexData:
        """Create an instance of ReindexData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReindexData.parse_obj(obj)

        _obj = ReindexData.parse_obj({
            "type": obj.get("type"),
            "truncate": obj.get("truncate"),
            "include_date": obj.get("includeDate"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to")
        })
        return _obj
