import requests
import os
import argparse

from dotenv import load_dotenv
from shared import get_image, files_ext


def fetch_nasa_apod():
    parser = argparse.ArgumentParser(
        description='Downloads NASA photo of day'
        )
    parser.add_argument('folder',
                        type=str,
                        help='Output dir for image'
                        )
    parser.add_argument('-count',
                        type=int,
                        default=10,
                        help='Count randomly chosen images (default 10)'
                        )
    args = parser.parse_args()
    load_dotenv()
    nasa_key = os.environ["NASA_API_KEY"]
    nasa_params = {"api_key": nasa_key,
                   "count": args.count
                   }
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    nasa_response = requests.get(nasa_url, params=nasa_params)
    nasa_response.raise_for_status()
    link_list = nasa_response.json()
    for link_number, link in enumerate(link_list):
        try:
            ext = files_ext(link["hdurl"])
        except KeyError:
            continue
        path = f'{args.folder}/nasa_apod{link_number}{ext}'
        get_image(link["hdurl"], path)


def main():
    fetch_nasa_apod()


if __name__ == '__main__':
    main()
