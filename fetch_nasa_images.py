import os.path
from pathlib import Path

import requests
from dotenv import load_dotenv

from download_image import download_image
from determine_file_extension import determine_file_extension


def get_pictures_nasa_day(photos_number, nasa_key, name_folder):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
      'count': photos_number,
      'api_key': nasa_key
    }
  
    response = requests.get(url, params=params)
    nasa_images = response.json()
    for images_numbers, nasa_image in enumerate(nasa_images):
        if not nasa_image['url']:
            continue
        image_link = nasa_image['url']
        extension = determine_file_extension(image_link)
        filename = os.path.join(images_numbers, extension)
        file_path = os.path.join(name_folder, filename)
        download_image(image_link, file_path)


def main():
    load_dotenv()
    nasa_key = os.getenv('NASA_KEY')
    name_folder = 'media'
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    photos_number = 30
    get_pictures_nasa_day(photos_number, nasa_key, name_folder)


if __name__ == '__main__':
    main()
