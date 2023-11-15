from datetime import UTC, datetime
from uuid import UUID

import pytest
from freezegun import freeze_time

from python_package_publish.utils import get_utc_now, get_uuid


def test_get_uuid_is_valid_uuid() -> None:
    """Test that get_uuid() returns a valid uuid."""
    try:
        UUID(get_uuid())
    except ValueError:
        pytest.fail("get_uuid() did not return a valid uuid.")


@freeze_time("1955-11-12 06:38:00")
def test_get_utc_now() -> None:
    """Test that get_utc_now() returns the current utc datetime."""
    now: datetime = get_utc_now()

    assert now == datetime(
        year=1955, month=11, day=12, hour=6, minute=38, second=0, tzinfo=UTC
    )
