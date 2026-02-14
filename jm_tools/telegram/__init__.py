import requests
import logging


def send_telegram_message(token, chat_id, message):
    bot_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    bot_request = requests.get(bot_url)
    if bot_request.status_code < 400:
        logging.info(f"Message sent")
    else:
        logging.error(f"Exception sending Telegram message - {bot_request.status_code}: {bot_request.text}")
