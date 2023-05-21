import datetime
import os.path
from pathlib import Path

import requests
from dotenv import load_dotenv

from download_image import download_image
from determine_file_extension import determine_file_extension


def get_pictures_epic(nasa_key, name_folder):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
      'api_key': nasa_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for number, nasa_image in enumerate(nasa_images):
        publish_date = nasa_image['date']
        image_name = nasa_image['image']
        image_date_format = datetime.datetime.fromisoformat(publish_date).strftime('%Y/%m/%d')
        image_url =   f'https://api.nasa.gov/EPIC/archive/natural/{image_date_format}/png/{image_name}.png'
        extension = determine_file_extension(image_url)
        filename = os.path.join(number, extension)
        file_path = os.path.join(name_folder, filename)
        download_image(image_url, file_path, params)

     
def main():
    load_dotenv()
    nasa_key = os.getenv('NASA_KEY')
    name_folder = 'media'
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    get_picture_epic(nasa_key, name_folder)
  

if __name__ == '__main__':
    main()
