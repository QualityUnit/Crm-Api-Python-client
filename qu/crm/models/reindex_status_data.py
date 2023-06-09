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
from pydantic import BaseModel, StrictBool, conlist
from qu.crm.models.index_status import IndexStatus

class ReindexStatusData(BaseModel):
    """
    ReindexStatusData
    """
    elastic_active: Optional[StrictBool] = None
    index_status: Optional[conlist(IndexStatus)] = None
    __properties = ["elastic_active", "index_status"]

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
    def from_json(cls, json_str: str) -> ReindexStatusData:
        """Create an instance of ReindexStatusData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in index_status (list)
        _items = []
        if self.index_status:
            for _item in self.index_status:
                if _item:
                    _items.append(_item.to_dict())
            _dict['index_status'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReindexStatusData:
        """Create an instance of ReindexStatusData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReindexStatusData.parse_obj(obj)

        _obj = ReindexStatusData.parse_obj({
            "elastic_active": obj.get("elastic_active"),
            "index_status": [IndexStatus.from_dict(_item) for _item in obj.get("index_status")] if obj.get("index_status") is not None else None
        })
        return _obj

