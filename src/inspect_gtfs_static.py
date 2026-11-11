import csv
from pathlib import Path
from zipfile import ZipFile

archive_path = Path("data/bronze/sl/gtfs_static/2026-08-26.zip")
target_trip_id = "14010000716081755"

with ZipFile(archive_path) as archive:
    with archive.open("trips.txt") as file:
        reader = csv.DictReader(
            line.decode("utf-8-sig") for line in file
        )

        trip = next(
            (row for row in reader if row["trip_id"] == target_trip_id),
            None,
        )

if trip:
    print("Trip found!")
    print("Trip ID:", trip["trip_id"])
    print("Route ID:", trip["route_id"])
    print("Service ID:", trip["service_id"])
    print("Headsign:", trip.get("trip_headsign"))
    print("Direction:", trip.get("direction_id"))

    with ZipFile(archive_path) as archive:
        with archive.open("routes.txt") as file:
            reader = csv.DictReader(
                line.decode("utf-8-sig") for line in file
            )

            route = next(
                (row for row in reader if row["route_id"] == trip["route_id"]),
                None,
            )

    if route:
        print("\nRoute information:")
        print("Short name:", route.get("route_short_name"))
        print("Long name:", route.get("route_long_name"))
        print("Route type:", route.get("route_type"))
    else:
        print("Route not found")

else:
    print("Trip not found in GTFS Static")




from io import TextIOWrapper

target_sequences = {"19", "32"}

with ZipFile(archive_path) as archive:
    with archive.open("stop_times.txt") as file:
        reader = csv.DictReader(
            TextIOWrapper(file, encoding="utf-8-sig")
        )

        for row in reader:
            if (
                row["trip_id"] == target_trip_id
                and row["stop_sequence"] in target_sequences
            ):
                print("\nStop sequence:", row["stop_sequence"])
                print("Stop ID:", row["stop_id"])
                print("Scheduled arrival:", row["arrival_time"])
                print("Scheduled departure:", row["departure_time"])


with ZipFile(archive_path) as archive:
    with archive.open("agency.txt") as file:
        reader = csv.DictReader(
            TextIOWrapper(file, encoding="utf-8-sig")
        )

        timezones = {row["agency_timezone"] for row in reader}

print("\nAgency timezones:", timezones)


