import asyncio

import telebot
from telebot import StateMemoryStorage, StatePickleStorage

ststorage = StatePickleStorage()
state_storage = StateMemoryStorage()


bot = telebot.TeleBot(state_storage=ststorage, token="6016281493:AAEIcbTY5adYAHn2rA6j2Kl8_KzTMD3iTdw",
                      parse_mode='HTML',
                      disable_web_page_preview=True, allow_sending_without_reply=True,
                      disable_notification=False, protect_content=False, skip_pending=True)
#TOKEN = "6016281493:AAEIcbTY5adYAHn2rA6j2Kl8_KzTMD3iTdw"
TOKEN='5946610713:AAE761arRr9sFXcj-Aq6rkrZ1A9xX0tJvzE'
bnusers = []  # Айди забаненных людей
adm_id = [5988273096]  # Айди администратора
adm_chat = 5988273096  # тоже айди администратора, первый используется для проверки фильтра как чат айди, а второй
# для методов
adm_chat2 =5649067326
admin_chat_id = 5988273096
admin_id_spam=5988273096
