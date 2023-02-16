import telegram
import os
import argparse
import random

from dotenv import load_dotenv
from time import sleep


def schedule():
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
        default=14400,
        help='Timer, sec.')
    args = parser.parse_args()
    load_dotenv()
    list_photo = list(os.walk(args.photo_folder))[0][2]
    while True:
        for photo in list_photo:
            publish_photo(os.path.join(args.photo_folder,photo))
            sleep(timer)
        random.shuffle(list_photo)


def publish_photo(photo):
    bot_token = os.environ["BOT_TOKEN"]
    space_bot = telegram.Bot(token=bot_token)
    chat_id = os.environ["CHANEL_ID"]
    with open(photo, 'rb') as image_file:
        space_bot.send_document(chat_id=chat_id, document=image_file)


def main():
    schedule()

if __name__ == '__main__':
    main()