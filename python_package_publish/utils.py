import datetime as _datetime
import uuid as _uuid


def get_uuid() -> str:
    """Produces a string uuid4 when provided as the default value within
    a SQLAlchemy model. Also used to produce deterministic UUIDs when
    generation new models during testing.
    """
    return str(_uuid.uuid4())


def get_utc_now() -> _datetime.datetime:
    """Produces the current datetime as UTC when provided as a default within
    a SQLAlchemy model. Also used to freeze datetime via freezegun during testing.
    """
    return _datetime.datetime.now(_datetime.UTC)
