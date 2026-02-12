# visuals_fetcher.py

import requests
import os

PEXELS_API_KEY = "MoPCuvXVev78gJs6xgAx9MOMjoVT14szGLl24rRfPBYKk8Gqg49a5lWq"

def fetch_video_from_pexels(query, output_dir="assets/videos"):
    os.makedirs(output_dir, exist_ok=True)
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": 1}
    url = "https://api.pexels.com/videos/search"

    response = requests.get(url, headers=headers, params=params).json()
    video_url = response["videos"][0]["video_files"][0]["link"]
    
    output_path = os.path.join(output_dir, f"{query.replace(' ', '_')}.mp4")
    
    with open(output_path, "wb") as f:
        f.write(requests.get(video_url).content)
    
    return output_path
