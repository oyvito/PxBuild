# generated by datamodel-codegen:
#   filename:  pxcodes.yaml
#   timestamp: 2023-09-20T14:42:31+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Admin(BaseModel):
    is_final: Optional[bool] = Field(None, alias='isFinal', example=True)
    tags: Optional[List[str]] = None
    todo_creation: Optional[str] = Field(None, alias='todoCreation')


class SortGroupingsOn(Enum):
    """
    Sets the order of the groupings in the dropdown
    """

    filename_base = 'filenameBase'
    label = 'label'
    rank = 'rank'


class SortValueitemsOn(Enum):
    code = 'code'
    label = 'label'
    rank = 'rank'


class Note(BaseModel):
    text: Dict[str, str]
    is_mandatory: bool = Field(..., alias='isMandatory')


class Valueitem(BaseModel):
    code: Optional[str] = Field(None, example='123234a')
    unordered_children: Optional[List[str]] = Field(None, alias='unorderedChildren')
    """
    Any children in random order. The children MUST exist in root-valueitems
    """
    label: Optional[Dict[str, str]] = None
    rank: Optional[Dict[str, str]] = None
    notes: Optional[List[Note]] = None


class Grouping(BaseModel):
    filename_base: Optional[str] = Field(None, alias='filenameBase')
    label: Optional[Dict[str, str]] = None
    rank: Optional[Dict[str, str]] = None
    sort_valueitems_on: Optional[SortValueitemsOn] = Field(
        None, alias='sortValueitemsOn'
    )
    """
    How to sort the list of mothers. The children will be sorted by the root-sortValueitemsOn
    """
    valueitems: Optional[List[Valueitem]] = None
    """
    The mothers
    """


class PxCodes(BaseModel):
    """
    For one variable, this should hold all the information needed to create vs and agg files and the VALUES and CODES px-keywords, and partially for elimination.
    """

    id: str = Field(..., example='123234a')
    admin: Optional[Admin] = None
    sort_valueitems_on: SortValueitemsOn = Field(..., alias='sortValueitemsOn')
    label: Optional[Dict[str, str]] = None
    valueitems: List[Valueitem]
    elimination_possible: bool = Field(..., alias='eliminationPossible', example=True)
    """
    May this variable be eliminnated. If True and eliminationCode is empty use Sum.
    """
    elimination_code: Optional[str] = Field(
        None, alias='eliminationCode', example='tot'
    )
    """
    Value is the code to use for eliminnating the variable
    """
    sort_groupings_on: Optional[SortGroupingsOn] = Field(None, alias='sortGroupingsOn')
    """
    Sets the order of the groupings in the dropdown
    """
    groupings: Optional[List[Grouping]] = None
    """
    List where an element is a grouping. A grouping is a list of mothers. The code of a mother must not be present in the root-valueitems. The children of a mother must be present in the root-valueitems and must be a unique list. The child may have many mothers.
    """
