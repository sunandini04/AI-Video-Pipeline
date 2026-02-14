import requests
import os

PEXELS_API_KEY = "MoPCuvXVev78gJs6xgAx9MOMjoVT14szGLl24rRfPBYKk8Gqg49a5lWq"  

def fetch_video_from_pexels(query, output_dir="assets/videos"):
    os.makedirs(output_dir, exist_ok=True)

    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": 1}
    url = "https://api.pexels.com/videos/search"

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch video from Pexels.")

    data = response.json()

    if not data.get("videos"):
        raise Exception("No videos found for this topic on Pexels.")

    video_files = data["videos"][0].get("video_files")

    if not video_files:
        raise Exception("No downloadable video files found.")

    video_url = video_files[0]["link"]

    output_path = os.path.join(output_dir, f"{query.replace(' ', '_')}.mp4")

    video_response = requests.get(video_url)

    with open(output_path, "wb") as f:
        f.write(video_response.content)

    return output_path
