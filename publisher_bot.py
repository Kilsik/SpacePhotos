import os
import argparse
import random

from time import sleep
from dotenv import load_dotenv
from shared import publish_photo


def scheduled_publishing():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Publish docs from folders according to the schedule'
        )
    parser.add_argument(
        'photo_folder',
        help='Folder with photos'
        )
    parser.add_argument(
        '-timer',
        type=int,
        default=os.environ["TIMER"],
        help='Timer, sec.')
    args = parser.parse_args()
    list_photo = list(os.walk(args.photo_folder))[0][2]
    timer = args.timer
    while True:
        for photo in list_photo:
            publish_photo(os.path.join(args.photo_folder, photo))
            sleep(timer)
        random.shuffle(list_photo)


def main():
    scheduled_publishing()


if __name__ == '__main__':
    main()
