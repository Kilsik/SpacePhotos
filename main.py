import requests
import os
import datetime

from dotenv import load_dotenv
from pathlib import Path
from urllib import parse



def get_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(folder):
    latest_launch_url = 'https://api.spacexdata.com/v5/launches/latest'
    launch_response = requests.get(latest_launch_url)
    launch_response.raise_for_status()
    #print(response.json())
    if launch_response.json()['links']['flickr']['original']:
        launch_id = response.json()["id"]  # это на случай, если пуск с картинками
    else:
        launch_id = '5eb87d47ffd86e000604b38a'  # если картинок нет
        launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        launch_response = requests.get(launch_url)
        launch_response.raise_for_status()
    link_list = launch_response.json()['links']['flickr']['original']
    for link_number, link in enumerate(link_list):
        path = f'{folder}/SpaceX{link_number}.jpg'
        get_image(link, path)


def fetch_nasa_apod(folder):
    nasa_key = os.environ["NASA_API_KEY"]
    nasa_params = {"api_key": nasa_key,
                    "count": 50
    }
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    nasa_response = requests.get(nasa_url, params=nasa_params)
    nasa_response.raise_for_status()
    link_list = nasa_response.json()
    for link_number, link in enumerate(link_list):
        try:
            ext = files_ext(link["hdurl"])
        except:
            continue
        path = f'{folder}/nasa_apod{link_number}{ext}'
        get_image(link["hdurl"], path)


def fetch_nasa_epic(folder):
    nasa_key = os.environ["NASA_API_KEY"]
    epic_param = {"api_key": nasa_key}
    epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    arg = input("Input 'all', 'YYYY-MM-DD' or 'images'")
    full_url = f'{epic_url}/{arg}'
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
        path = f'{folder}/nasa_epic{pic[0]}.png'
        get_image(pic_url, path)


def files_ext(pic_url):
    split_url = parse.urlparse(parse.unquote(pic_url))
    file_name = os.path.split(split_url[2])[1]
    ext = os.path.splitext(file_name)[1]
    return ext


def main():
    load_dotenv()
    imgs_folder = 'images'
    Path(imgs_folder).mkdir(exist_ok=True)
    fetch_spacex_last_launch(imgs_folder)
    fetch_nasa_apod(imgs_folder)
    fetch_nasa_epic(imgs_folder)

if __name__ == '__main__':
    main()
