import datetime
from uuid import UUID

from python_package_publish.utils import get_utc_now, get_uuid


def test_get_uuid() -> None:
    """Test that get_uuid() returns a valid uuid."""
    UUID(get_uuid())


def test_get_utc_now() -> None:
    """Test that get_utc_now() returns the current utc datetime."""
    now = get_utc_now()
    assert now.tzinfo == datetime.UTC
