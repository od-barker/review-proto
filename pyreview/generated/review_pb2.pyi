from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Rating(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXCELLENT: _ClassVar[Rating]
    GOOD: _ClassVar[Rating]
    OK: _ClassVar[Rating]
    MEH: _ClassVar[Rating]
    BOGUS: _ClassVar[Rating]
EXCELLENT: Rating
GOOD: Rating
OK: Rating
MEH: Rating
BOGUS: Rating

class MyResponse(_message.Message):
    __slots__ = ("saved",)
    SAVED_FIELD_NUMBER: _ClassVar[int]
    saved: bool
    def __init__(self, saved: bool = ...) -> None: ...

class MyReview(_message.Message):
    __slots__ = ("userid", "timestamp", "message", "rating")
    USERID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    userid: int
    timestamp: int
    message: str
    rating: Rating
    def __init__(self, userid: _Optional[int] = ..., timestamp: _Optional[int] = ..., message: _Optional[str] = ..., rating: _Optional[_Union[Rating, str]] = ...) -> None: ...
