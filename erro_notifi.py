

from loader import bot, adm_chat, adm_chat2
import requests
import asyncio
#bot = telebot.TeleBot(token="6016281493:AAEIcbTY5adYAHn2rA6j2Kl8_KzTMD3iTdw")
server_url = "https://api.td-market.md/admin/test-server"

def send_message(chat_id,error_message):
    bot.send_message(chat_id, error_message)

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
        send_message(adm_chat,error_message)

async def check_SERVER():
    while True:
        result =await send_request()
        if result is True:
            await asyncio.sleep(1)
            print("начал")

        else:
            send_message(adm_chat, "упал" )  # Отправляем текст ошибки
            send_message(adm_chat2,"упал")  # Отправляем текст ошибки
            await asyncio.sleep(1)
            print("упал")


#bot.infinity_polling()
