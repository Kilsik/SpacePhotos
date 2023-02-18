import os
import argparse
import random

from time import sleep
from dotenv import load_dotenv
from shared import publish_photo


def publish_contet(bot_token, chat_id, folder, timer):
    *__, last_photos = list(os.walk(folder))
    *__, photos = last_photos
    while True:
        for photo in photos:
            publish_photo(bot_token, chat_id, os.path.join(folder, photo))
            sleep(timer)
        random.shuffle(photos)


def main():
    load_dotenv()
    chat_id = os.environ["TELEGRAM_CHANEL_ID"]
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
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
    publish_contet(bot_token, chat_id, args.photo_folder, args.timer)


if __name__ == '__main__':
    main()
