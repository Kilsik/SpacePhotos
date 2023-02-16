import telegram
import os
import argparse

from dotenv import load_dotenv


def publish(text, photo):
    load_dotenv()
    bot_token = os.environ["BOT_TOKEN"]
    space_bot = telegram.Bot(token=bot_token)
    chat_id = os.environ["CHANEL_ID"]
    with open(text, 'r') as text_file:
        text_message = text_file.read()
    space_bot.send_message(chat_id=chat_id, text=text_message)
    with open(photo, 'rb') as image_file:
        space_bot.send_document(chat_id=chat_id, document=image_file)


def main():
    #image = 'images/nasa_apod1.jpg'
    #space_bot.send_document(chat_id=chat_id, document=open(image, 'rb'))
    publish('texts/Artemis 1_1.txt', 'images/nasa_apod1.jpg')

if __name__ == '__main__':
    main()