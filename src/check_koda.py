import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TRAFIKLAB_API_KEY")

if not api_key:
    raise RuntimeError("TRAFIKLAB_API_KEY is missing")

url = "https://api.koda.trafiklab.se/KoDa/api/v2/gtfs-rt/sl/TripUpdates"

params = {
    "date": "2026-08-26",
    "key": api_key,
}

response = requests.head(
    url,
    params=params,
    timeout=30,
    allow_redirects=True,
)

print("HTTP status:", response.status_code)
print("Content-Length:", response.headers.get("Content-Length"))
print("Content-Type:", response.headers.get("Content-Type"))

response.close()
