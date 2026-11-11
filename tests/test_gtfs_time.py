
from datetime import datetime, timezone

from src.gtfs_time import parse_gtfs_datetime


def test_normal_gtfs_time():
    result = parse_gtfs_datetime("20260826", "22:17:00")

    assert result.year == 2026
    assert result.month == 8
    assert result.day == 26
    assert result.hour == 22
    assert result.minute == 17
    assert result.utcoffset().total_seconds() == 7200


def test_gtfs_time_after_midnight():
    result = parse_gtfs_datetime("20260826", "25:30:00")

    assert result.year == 2026
    assert result.month == 8
    assert result.day == 27
    assert result.hour == 1
    assert result.minute == 30


def test_actual_sl_delay():
    scheduled = parse_gtfs_datetime("20260826", "22:17:00")
    observed = datetime.fromtimestamp(
        1787780963, tz=timezone.utc
    )

    delay_seconds = (observed - scheduled).total_seconds()

    assert delay_seconds == 5543
