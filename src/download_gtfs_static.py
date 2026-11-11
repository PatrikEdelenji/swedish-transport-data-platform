import os

from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TRAFIKLAB_API_KEY")

if not api_key:
    raise RuntimeError("TRAFIKLAB_API_KEY is missing")

url = "https://api.koda.trafiklab.se/KoDa/api/v2/gtfs-static/sl"

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


destination = Path("data/bronze/sl/gtfs_static/2026-08-26.zip")
destination.parent.mkdir(parents=True, exist_ok=True)

with requests.get(url, params=params, stream=True, timeout=(10, 120)) as response:
    if response.status_code != 200:
        raise RuntimeError(f"Unexpected HTTP status: {response.status_code}")

    with destination.open("wb") as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)

print(f"Downloaded: {destination.stat().st_size:,} bytes")

response.close()
