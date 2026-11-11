from pathlib import Path
from google.transit import gtfs_realtime_pb2

file_path = Path(
    "data/temp/sample/sl/TripUpdates/2026/08/26/23/"
    "sl-tripupdates-2026-08-26T23-58-42Z.pb"
)

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(file_path.read_bytes())

print("Total entities:", len(feed.entity))

trip_updates = [
    entity.trip_update
    for entity in feed.entity
    if entity.HasField("trip_update")
]

print("TripUpdates:", len(trip_updates))

if trip_updates:
    update = trip_updates[0]

    print("Trip ID:", update.trip.trip_id)
    print("Start date:", update.trip.start_date)
    print("StopTimeUpdates:", len(update.stop_time_update))
