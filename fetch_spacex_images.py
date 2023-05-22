import os.path
import argparse
from pathlib import Path

import requests

from download_image import download_image
from pprint import pprint

def fetch_spacex_last_launch(url):
    name_folder = 'media'
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()
    if images['links']['flickr_images']:
        images_link = images['links']['flickr_images']
    for image_number, image_link in enumerate(images_link):
        filename = f'spacex{image_number}.jpg'
        file_path = os.path.join(name_folder, filename)
        download_image(image_link, file_path)


def main():
    parser = argparse.ArgumentParser(description='Программа для скачиваний изображений космоса с сайта NASA')
    parser.add_argument(
        '--id', 
        help='Указать свой id запуска для скачивания изображений',
        default='5eb87d42ffd86e000604b384')
    args = parser.parse_args()
    url = f'https://api.spacexdata.com/v3/launches/{args.id}'
    fetch_spacex_last_launch(url)
    
    
if __name__ == '__main__':
    main()
