import requests
import os

from pathlib import Path
from urllib import parse


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



def main():
    pass

if __name__ == '__main__':
    main()
