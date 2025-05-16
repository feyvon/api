import requests
import argparse
from main import download_image


def main():
    parser = argparse.ArgumentParser(description="Скачивает изображения SpaceX")
    parser.add_argument('--id', help="ID запуска SpaceX", default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    url = f"https://api.spacexdata.com/v5/launches/{args.id}"
    response = requests.get(url)
    response.raise_for_status()
    photos = response.json()["links"]["flickr"]["original"]
    for photonumber, photourl in enumerate(photos):
        filename = f"spacex_{photonumber}.jpg"
        download_image(photourl, "images", filename)


if __name__ == "__main__":
    main()