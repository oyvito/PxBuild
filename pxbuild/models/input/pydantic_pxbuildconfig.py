# generated by datamodel-codegen:
#   filename:  pxbuildconfig.yaml
#   timestamp: 2024-01-25T12:22:57+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, constr


class ResourceType(Enum):
    file = 'file'
    s3_todo = 's3_todo'
    api_todo = 'api_todo'


class PxMetadataResource(BaseModel):
    """
    What resource provides the pxmetdata-json
    """

    resource_type: Optional[ResourceType] = Field('file', alias='resourceType')
    adress_format: str = Field(..., alias='adressFormat')
    """
    The path or url to the json, given its id. Example: example_data/pxmetadata/{id}.json
    """


class PxStatisticsResource(BaseModel):
    """
    What resource provides the pxstatistics-json
    """

    resource_type: Optional[ResourceType] = Field('file', alias='resourceType')
    adress_format: str = Field(..., alias='adressFormat')
    """
    The path or url to the json, given its id. Example: example_data/pxstatistics/pxstatistics_{id}.json
    """


class PxCodesResource(BaseModel):
    """
    What resource provides the pxcodes-json
    """

    resource_type: Optional[ResourceType] = Field('file', alias='resourceType')
    adress_format: str = Field(..., alias='adressFormat')
    """
    The path or url to the json, given its id. Example: example_data/pxcodes/{id}.json
    """


class PxDataResource(BaseModel):
    """
    What resource provides the datadata
    """

    resource_type: Optional[ResourceType] = Field('file', alias='resourceType')
    adress_format: str = Field(..., alias='adressFormat')
    """
    The path or url to the json, given its id. Example: example_data/parquet_files/{id}
    """


class ResourceType4(Enum):
    folders = 'folders'
    s3_todo = 's3_todo'
    dictionary_todo = 'dictionary_todo'


class OutputDestination(BaseModel):
    """
    Where to send the output
    """

    resource_type: Optional[ResourceType4] = Field('folders', alias='resourceType')
    px_folder_format: Optional[str] = Field(None, alias='pxFolderFormat')
    """
    Aplies to resourcetype=folders. The folder where the .px-files are written. id is the tableID. Example: example_data/pxbuild_output/{id}
    """
    agg_folder_format: Optional[str] = Field(None, alias='aggFolderFormat')
    """
    Aplies to resourcetype=folders. The folder where the .vs- and .agg-files are written. id is the tableID. Example: example_data/pxbuild_output/id}
    """


class Admin(BaseModel):
    """
    These properties does not enter the pxfile directly
    """

    px_metadata_resource: PxMetadataResource = Field(..., alias='pxMetadataResource')
    """
    What resource provides the pxmetdata-json
    """
    px_statistics_resource: PxStatisticsResource = Field(..., alias='pxStatisticsResource')
    """
    What resource provides the pxstatistics-json
    """
    px_codes_resource: PxCodesResource = Field(..., alias='pxCodesResource')
    """
    What resource provides the pxcodes-json
    """
    px_data_resource: PxDataResource = Field(..., alias='pxDataResource')
    """
    What resource provides the datadata
    """
    output_destination: OutputDestination = Field(..., alias='outputDestination')
    """
    Where to send the output
    """
    valid_languages: List[str] = Field(..., alias='validLanguages')
    """
    The 2-letter languagecodes. Probably ISO 639, but the real constraint is that it has to match your pxweb
    """
    build_multilingual_files: Optional[bool] = Field(True, alias='buildMultilingualFiles')
    """
    make multilingual PX-files, not one for each language. If true, the first entry in validLanguages will be used for language keyword.
    """
    skip_creation_date: Optional[bool] = Field(False, alias='skipCreationDate')
    """
    should the CREATION-DATE keyword be skipped. Usefull (only) for pytests that compare PX-files.
    """
    the_word_and: Dict[str, str] = Field(..., alias='theWordAnd')
    the_word_by: Dict[str, str] = Field(..., alias='theWordBy')


class PxbuildConfig(BaseModel):
    admin: Admin
    """
    These properties does not enter the pxfile directly
    """
    charset: Optional[constr(max_length=20)] = None
    """
    example: ANSI
    """
    axis_version: Optional[constr(max_length=20)] = Field(None, alias='axisVersion')
    """
    Version of px-file format.  example: '2013'
    """
    code_page: Optional[constr(max_length=20)] = Field('iso-8859-1', alias='codePage')
    """
    example: iso-8859-1
    """
    description_default: Optional[bool] = Field(False, alias='descriptionDefault')
    contvariable: Optional[Dict[str, constr(max_length=256)]] = None
    """
    Name for content variable
    """
    contvariable_code: Optional[str] = Field('ContentCode', alias='contvariableCode')
    """
    Code for content variable
    """
    timevariable_code: Optional[str] = Field('Time', alias='timevariableCode')
    """
    Code for the time variable
    """
    datasymbol1: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol2: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol3: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol4: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol5: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol6: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol_nil: Optional[Dict[str, constr(max_length=20)]] = Field(None, alias='datasymbolNil')
    """
    How stored - are shown on screen
    """
    datasymbol_sum: Optional[Dict[str, constr(max_length=20)]] = Field(None, alias='datasymbolSum')
    """
    This if used to indicate how a sum of differing numbers of dots will be shown. The sum is stored as “…….”.
    """
    source: Optional[Dict[str, constr(max_length=256)]] = None
    """
    Name for content variable
    """