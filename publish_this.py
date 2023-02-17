import random
import argparse
import os

from shared import publish_photo


def publish_this():
    parser = argparse.ArgumentParser(
        description='Publishes the specified photo to the channel'
        )
    parser.add_argument("-f", "--file", default=None)
    args = parser.parse_args()
    if args.file:
        photo = args.file
    else:
        list_photo = list(os.walk('images'))[0][2]
        photo = os.path.join('images', random.choice(list_photo))
    publish_photo(photo)


def main():
    publish_this()


if __name__ == '__main__':
    main()
