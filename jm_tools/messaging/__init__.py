import logging
import requests
from jm_tools.config.telegram import TELEGRAM_TOKEN


def send_telegram_message(telegram_chat_id, message):
    bot_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={telegram_chat_id}&text={message}"
    bot_request = requests.get(bot_url)
    if bot_request.status_code < 400:
        logging.error(f"Message sent")
    else:
        logging.error(f"Exception sending Telegram - {bot_request.status_code}: {bot_request.text}")
