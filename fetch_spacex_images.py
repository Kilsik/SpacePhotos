import requests
import argparse

from shared import get_image


def fetch_spacex_last_launch():
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
    if args.lid:
        launch_id = args.lid
        launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        launch_url = 'https://api.spacexdata.com/v5/launches/latest'
    launch_response = requests.get(launch_url)
    launch_response.raise_for_status()
    if launch_response.json()['links']['flickr']['original']:
        link_list = launch_response.json()['links']['flickr']['original']
        for link_number, link in enumerate(link_list):
            path = f'{args.folder}/SpaceX{link_number}.jpg'
            get_image(link, path)
    else:
        if args.lid:
            print('There are not images on this launch')
        else:
            print('There are not images on latest launch')


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
