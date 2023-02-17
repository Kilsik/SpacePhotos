import requests
import argparse

from shared import get_image


def fetch_spacex_launch(folder, launch_id):
    launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    launch_response = requests.get(launch_url)
    launch_response.raise_for_status()
    if not launch_response.json()['links']['flickr']['original']:
        print('There are not images on this launch')
        return
    link_roster = launch_response.json()['links']['flickr']['original']
    for link_number, link in enumerate(link_roster):
        path = f'{folder}/SpaceX{link_number}.jpg'
        get_image(link, path)
    return


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
        help='Launch id',
        default='latest'
        )
    args = parser.parse_args()
    fetch_spacex_launch(args.folder, args.lid)


if __name__ == '__main__':
    main()
