import telegram
import requests
import os
import pathlib

from urllib import parse


def get_image(url, path):
    folder = pathlib.PurePath(path).parent
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_files_ext(pic_url):
    split_url = parse.urlparse(parse.unquote(pic_url))
    file_name = os.path.split(split_url[2])[1]
    ext = os.path.splitext(file_name)[1]
    return ext


def publish_photo(bot_token, chat_id, photo):
    space_bot = telegram.Bot(token=bot_token)
    with open(photo, 'rb') as image_file:
        space_bot.send_document(chat_id=chat_id, document=image_file)
