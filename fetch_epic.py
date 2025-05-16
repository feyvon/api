import requests
import datetime
from main import download_image


def main():
    api_key = "ukhBYrlzWV8nvsfCVtio3sSpIDFBcqPGViOidtY5"
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    for photonumber, i in enumerate(response.json()):
        date = datetime.datetime.strptime(i["date"], "%Y-%m-%d %H:%M:%S")
        formatted_date = date.strftime("%Y/%m/%d")
        imagename = i["image"]
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{imagename}.png?api_key={api_key}"
        download_image(epic_url, "images", filename= f"epic_{photonumber}.png")


if __name__ == "__main__":
    main()