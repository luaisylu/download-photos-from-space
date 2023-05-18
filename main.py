import os
import argparse
import random
import time

import telegram
from dotenv import load_dotenv


def publish_media_in_telegram(telegram_token, telegram_channel_chat_id, args):
    bot = telegram.Bot(token=telegram_token)
    images = sorted(os.listdir("media"))
    random.shuffle(images)
    while True:
        random.shuffle(images)
        for image in images:
            image_path = os.path.join('media', image)
            with open(image_path, 'rb') as file:
         
                photo = file
                bot.send_document(chat_id=telegram_channel_chat_id, document=photo)
            time.sleep(args.publication_time)


def main():
    parser = argparse.ArgumentParser(
        description='Программа запрашивает через какой промежуток времени нужно публиковать изображения в телегарм канал'
    )
    parser.add_argument(
        '--publication_time',
        type=int,
        help='Частота публикации изображения',
        default=14440
    )
    args = parser.parse_args()

    load_dotenv()

    telegram_token = os.getenv("TG_TOKEN")
    telegram_channel_chat_id = os.getenv("TELEGRAM_CHANNEL_CHAT_ID")

    publish_media_in_telegram(telegram_token, telegram_channel_chat_id, args)


if __name__ == "__main__":
    main()
