import json
from datetime import datetime
from json import JSONDecodeError

from telebot.handler_backends import StatesGroup, State

from inlinekeyboard import gen_button
import requests

from loader import bot


class Mystate(StatesGroup):
    user_id = State()
    first_state = State()
    data_state = State()
    time_state = State()
    people_state = State()
    cheep_state = State()
    long_dilevery = State()
    another = State()
    bag = State()
    no_answer = State()
    admin_call_1 = State()
    seller_state = State()
    callback_staff = State()
    notification = State()
    notification1 = State()
    my_money=State()

@bot.message_handler(commands=['start'])
def wellcome(message):
    try:
        with open("users.json", 'r') as f_o:
            data_from_json = json.load(f_o)
        user_id = message.from_user.id
        username = message.from_user.first_name
        usersurname = message.from_user.last_name
        if str(user_id) not in data_from_json:
            data_from_json[user_id] = {"username": username,"usersurname": usersurname,"user_id":user_id}


        with open('users.json', 'w') as f_o:
            json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)

        bot.send_message(chat_id=message.chat.id,
                         text="Здравствуйте!  Я бот заботы и поддержки td-market. Хочу вам помочь!\n"
                              "Чаще всего я понимаю только кнопки, но могу и попросить вас написать что-то в "
                              "сообщении.\n\n\n"
                              "Чтобы запустить бота, нажмите «Продолжить🧐»", reply_markup=gen_button())

    except JSONDecodeError as err:
        requests.post(f"https://api.telegram.org/bot6016281493:AAEIcbTY5adYAHn2rA6j2Kl8_KzTMD3iTdw"
                      f"/sendMessage?chat_id=5988273096&text={datetime.now()}:::{err.__class__}:::{err}")
    user_idd= message.chat.id










