import requests
import os
import datetime
from urllib.parse import urlparse


def download_image(url, folderpath, filename):
    os.makedirs(folderpath, exist_ok=True)
    filepath = os.path.join(folderpath, filename)
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath


def get_extension(image_url): 
    return os.path.splitext(urlparse(image_url).path)[-1]
