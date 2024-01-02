"""
Custom types used for model validation
"""
import datetime
import json
from typing import Annotated

from pydantic import BeforeValidator, Field, PlainSerializer, UrlConstraints
from pydantic_core import Url

from .validators import empty_string_to_none, parse_json_string

AnyHttpURL = Annotated[
    Url,
    UrlConstraints(allowed_schemes=["http", "https"]),
    PlainSerializer(lambda x: str(x), return_type=str),
]
EasyVereinReference = Annotated[
    int | AnyHttpURL | None, BeforeValidator(empty_string_to_none)
]
PositiveIntWithZero = Annotated[int, Field(ge=0)]
Date = Annotated[
    datetime.date, PlainSerializer(lambda x: x.strftime("%Y-%m-%d"), return_type=str)
]
DateTime = Annotated[
    datetime.datetime,
    PlainSerializer(lambda x: x.strftime("%Y-%m-%dT%H:%M:%S"), return_type=str),
]
OptionsField = Annotated[
    list[str] | None,
    PlainSerializer(lambda x: json.dumps(x), return_type=str),
    BeforeValidator(parse_json_string),
    BeforeValidator(empty_string_to_none),
]
HexColor = Annotated[
    str | None,
    Field(min_length=7, max_length=7),
    BeforeValidator(empty_string_to_none),
]
