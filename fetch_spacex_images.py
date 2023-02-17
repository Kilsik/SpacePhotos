import requests
import argparse

from shared import get_image


def fetch_spacex_last_launch(folder, launch_id):
    if launch_id:
        launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        launch_url = 'https://api.spacexdata.com/v5/launches/latest'
    launch_response = requests.get(launch_url)
    launch_response.raise_for_status()
    if launch_response.json()['links']['flickr']['original']:
        link_roster = launch_response.json()['links']['flickr']['original']
        for link_number, link in enumerate(link_roster):
            path = f'{folder}/SpaceX{link_number}.jpg'
            get_image(link, path)
    else:
        if launch_id:
            print('There are not images on this launch')
        else:
            print('There are not images on latest launch')


def main():
    parser = argparse.ArgumentParser(description='Downloads SpaceX photos')
    parser.add_argument(
        'folder',
        type=str,
        help='Output dir for image'
        )
    parser.add_argument(
        '-lid',
        type=str,
        help='Launch id'
        )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.folder, args.lid)


if __name__ == '__main__':
    main()
