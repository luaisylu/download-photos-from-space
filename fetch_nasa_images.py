import os.path
from pathlib import Path

import requests
from dotenv import load_dotenv

from download_image import download_image
from determine_file_extension import determine_file_extension


def get_picture_nasa_day(nasa_key, name_folder):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
      "count": 30,
      "api_key": nasa_key
    }
  
    response = requests.get(url, params=params)
    images_nasa = response.json()
    for images_number, image_nasa in enumerate(images_nasa):
        if image_nasa["url"]:
            link_image = image_nasa["url"]
            extension = determine_file_extension(link_image)
            filename = f"nasa{images_number}{extension}"
            file_path = f"{name_folder}/{filename}"
            download_image(link_image, file_path)


def main():
    load_dotenv()
    nasa_key = os.getenv("NASA_KEY")
    name_folder = "media"
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    get_picture_nasa_day(nasa_key, name_folder)


if __name__ == "__main__":
    main()