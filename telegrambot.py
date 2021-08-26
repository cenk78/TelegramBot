import requests
import configparser

config = configparser.ConfigParser()
config.read("secrets.ini")
token = config["TelegramCredentials"]["token"]
chatID = config["TelegramCredentials"]["chatID"]


def telegram_bot_sendtext(bot_message):

    bot_token = token
    bot_chatID = chatID
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

    return response.json()
