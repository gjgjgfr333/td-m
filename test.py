import asyncio
import threading

import requests

from loader import bot, adm_chat, adm_chat2
server_url = "https://api.td-market.md/admin/test-server"

# Функция для отправки запросов на сервер
def send_to_server_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(check_SERVER())
def send_message(chat_id,error_message):
    bot.send_message(chat_id, error_message)
# Определение асинхронной функции check_SERVER()
async def check_SERVER():
    while True:
        result = await send_request()
        if result is True:
            await asyncio.sleep(60)
            print("начал")
        else:
            send_message(adm_chat, "упал")
            send_message(adm_chat2, "упал")
            await asyncio.sleep(2600)
            print("упал")

# Определение асинхронной функции send_request()
async def send_request():
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print("упал серв")
        error_message = f"Произошла ошибка: "
        send_message(adm_chat, error_message)

