import requests
import argparse
from main import download_image
from main import get_extension


def main():
    parser = argparse.ArgumentParser(description="Скачивает изображения Nasa APOD")
    parser.add_argument('--count', help="Кол-во изображений", default=30)
    args = parser.parse_args()
    api_key = "ukhBYrlzWV8nvsfCVtio3sSpIDFBcqPGViOidtY5"
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
        "count": args.count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    for photonumber, item in enumerate(response.json()):
        download_image(item["url"], "images", filename = f"nasa_apod_{photonumber}{get_extension(item["url"])}")


if __name__ == "__main__":
    main()


