import requests
import argparse
import datetime
import os

from dotenv import load_dotenv
from shared import get_image


def fetch_nasa_epic():
    parser = argparse.ArgumentParser(
        description='Downloads NASA EPIC photos'
        )
    parser.add_argument('folder',
        type=str,
        help='Output dir for image'
        )
    parser.add_argument(
        '-date',
        help='''Images for this date format YYYY-MM-DD
        or most recent images (if absent)'''
        )
    args = parser.parse_args()
    load_dotenv()
    nasa_key = os.environ["NASA_API_KEY"]
    epic_param = {"api_key": nasa_key}
    epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    if args.date:
        full_url = f'{epic_url}/date/{args.date}'
    else:
        full_url = f'{epic_url}/images'
    response = requests.get(epic_url, params=epic_param)
    response.raise_for_status()
    pic_list = response.json()
    for pic in enumerate(pic_list):
        nasa_url = 'https://epic.gsfc.nasa.gov/archive/natural'
        date = str(datetime.datetime.fromisoformat(pic[1]["date"])).split()
        split_date = date[0].split('-')
        date_path = f'{split_date[0]}/{split_date[1]}/{split_date[2]}/'
        file_name = pic[1]["image"]
        pic_url = f'{nasa_url}/{date_path}/png/{file_name}.png'
        path = f'{args.folder}/nasa_epic{pic[0]}.png'
        get_image(pic_url, path)


def main():
    fetch_nasa_epic()

if __name__ == '__main__':
    main()
