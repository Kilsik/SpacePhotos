import random
import argparse
import os

from shared import publish_photo
from dotenv import load_dotenv


def publish_this(bot_token, chat_id, file):
    if file:
        photo = file
    else:
        *__, last_photos = list(os.walk('images'))
        *__, photos = last_photos
        photo = os.path.join('images', random.choice(photos))
    publish_photo(bot_token, chat_id, photo)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Publishes the specified photo to the channel'
        )
    parser.add_argument("-f", "--file", default=None)
    args = parser.parse_args()
    chat_id = os.environ["TELEGRAM_CHANEL_ID"]
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    publish_this(bot_token, chat_id, args.file)


if __name__ == '__main__':
    main()
