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
from pydantic import BaseModel, StrictInt, StrictStr, conlist, validator
from qu.crm.models.billing_metric import BillingMetric

class PeriodPricing(BaseModel):
    """
    PeriodPricing
    """
    name: Optional[StrictStr] = None
    metrics: Optional[conlist(BillingMetric)] = None
    base_price: Optional[StrictInt] = None
    __properties = ["name", "metrics", "base_price"]

    @validator('name')
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('1m', '1y'):
            raise ValueError("must be one of enum values ('1m', '1y')")
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
    def from_json(cls, json_str: str) -> PeriodPricing:
        """Create an instance of PeriodPricing from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item in self.metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metrics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PeriodPricing:
        """Create an instance of PeriodPricing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeriodPricing.parse_obj(obj)

        _obj = PeriodPricing.parse_obj({
            "name": obj.get("name"),
            "metrics": [BillingMetric.from_dict(_item) for _item in obj.get("metrics")] if obj.get("metrics") is not None else None,
            "base_price": obj.get("base_price")
        })
        return _obj

