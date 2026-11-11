
import csv
from datetime import datetime
from io import TextIOWrapper
from pathlib import Path
from zipfile import ZipFile


archive_path = Path("data/bronze/sl/gtfs_static/2026-08-26.zip")

service_id = "507"
service_date = "20260826"

date = datetime.strptime(service_date, "%Y%m%d").date()
weekday = (
    "monday", "tuesday", "wednesday", "thursday",
    "friday", "saturday", "sunday"
)[date.weekday()]

is_active = False

with ZipFile(archive_path) as archive:
    with archive.open("calendar.txt") as file:
        reader = csv.DictReader(TextIOWrapper(file, encoding="utf-8-sig"))

        for row in reader:
            if row["service_id"] == service_id:
                is_active = (
                    row["start_date"] <= service_date <= row["end_date"]
                    and row[weekday] == "1"
                )
                break

    with archive.open("calendar_dates.txt") as file:
        reader = csv.DictReader(TextIOWrapper(file, encoding="utf-8-sig"))

        for row in reader:
            if (
                row["service_id"] == service_id
                and row["date"] == service_date
            ):
                if row["exception_type"] == "1":
                    is_active = True
                elif row["exception_type"] == "2":
                    is_active = False

print("Service ID:", service_id)
print("Date:", date)
print("Weekday:", weekday)
print("Service active:", is_active)
