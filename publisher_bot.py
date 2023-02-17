import os
import argparse
import random

from time import sleep
from dotenv import load_dotenv
from shared import publish_photo


def scheduled_publishing(bot_token, chat_id, folder, timer):
    *__, roster_photo = list(os.walk(folder))[0]
    while True:
        for photo in roster_photo:
            publish_photo(bot_token, chat_id, os.path.join(folder, photo))
            sleep(timer)
        random.shuffle(roster_photo)


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
    scheduled_publishing(bot_token, chat_id, args.photo_folder, args.timer)


if __name__ == '__main__':
    main()
