import os.path


def determine_file_extension(image_url):
    url, extension = os.path.splitext(image_url)
    return extension