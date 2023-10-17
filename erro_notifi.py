from loader import bot, adm_chat, adm_chat2
import requests
import time
import traceback

server_url = "https://api.td-market.md/admin/test-server"

def send_message(chat_id, error_message):
    bot.send_message(chat_id, f"Произошла ошибка: {error_message}")

def send_request():
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        error_message = traceback.format_exc()
        print(error_message)
        return error_message  # Возвращаем текст ошибки

while True:
    result = send_request()
    if result is True:
        time.sleep(5)
        print("начал")
    else:
        send_message(adm_chat, result)  # Отправляем текст ошибки
        send_message(adm_chat2, result)  # Отправляем текст ошибки
        time.sleep(5)
        print("упал")
