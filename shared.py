import telegram
import requests
import os

from pathlib import Path
from urllib import parse
from dotenv import load_dotenv


def get_image(url, path):
    Path(path.split('/')[0]).mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def files_ext(pic_url):
    split_url = parse.urlparse(parse.unquote(pic_url))
    file_name = os.path.split(split_url[2])[1]
    ext = os.path.splitext(file_name)[1]
    return ext


def publish_photo(photo):
    bot_token = os.environ["BOT_TOKEN"]
    space_bot = telegram.Bot(token=bot_token)
    chat_id = os.environ["CHANEL_ID"]
    with open(photo, 'rb') as image_file:
        space_bot.send_document(chat_id=chat_id, document=image_file)


def main():
    pass


if __name__ == '__main__':
    main()
