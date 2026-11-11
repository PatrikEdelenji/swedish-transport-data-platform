
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def parse_gtfs_datetime(service_date: str, gtfs_time: str) -> datetime:
    stockholm_tz = ZoneInfo("Europe/Stockholm")
    date = datetime.strptime(service_date, "%Y%m%d")
    hours, minutes, seconds = map(int, gtfs_time.split(":"))
    midnight = date.replace(tzinfo=stockholm_tz)

    return midnight + timedelta(
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )


if __name__ == "__main__":
    from datetime import timezone

    scheduled = parse_gtfs_datetime("20260826", "22:17:00")
    observed = datetime.fromtimestamp(1787780963, tz=timezone.utc)

    delay = (observed - scheduled).total_seconds()

    print("Scheduled:", scheduled)
    print("Observed:", observed)
    print("Delay:", delay, "seconds")