import argparse
from pathlib import Path

import requests

from download_image import download_image


def fetch_spacex_last_launch(url, name_folder, args_id):
  params ={
      "id": args_id
  }
  response = requests.get(url, params=params)
  response.raise_for_status()
  images = response.json()
  for image in images:
      if image["links"]["flickr_images"]:
          link_the_images = image["links"]["flickr_images"]
  for images_number, link_image in enumerate(link_the_images):
    filename = f"spacex{images_number}.jpg"
    file_path = f"{name_folder}/{filename}"
    download_image(link_image, file_path)


def main():
    parser = argparse.ArgumentParser(description='Программа для скачиваний изображений космоса с сайта NASA')
    parser.add_argument(
        '--id', 
        help='Указать свой id запуска для скачивания изображений',
        default='5eb87d42ffd86e000604b384')
    args = parser.parse_args()
    name_folder = "media"
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches/"
    fetch_spacex_last_launch(url, name_folder, args)
    
    
if __name__ == "__main__":
    main()
