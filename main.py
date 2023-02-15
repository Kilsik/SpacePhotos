import requests
import os
import datetime

from dotenv import load_dotenv
from pathlib import Path
from urllib import parse












def main():
    load_dotenv()
    imgs_folder = 'images'
    Path(imgs_folder).mkdir(exist_ok=True)
    fetch_spacex_last_launch(imgs_folder)
    fetch_nasa_apod(imgs_folder)
    fetch_nasa_epic(imgs_folder)

if __name__ == '__main__':
    main()
