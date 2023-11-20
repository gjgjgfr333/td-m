from loader import bot
import requests
from telebot import types
from start import Mystate
from inlinekeyboard import finish
server_url1 = "https://api.td-market.md/auth"
notify_endpoint1 = "/check-user"
data_list_user = []

@bot.message_handler(func=lambda message: True, state= Mystate.notification)
def handle_messages(message):

    user_data = data_list_user[-1]  # Получаем последний добавленный элемент списка
    if user_data['email'] is None:
        user_data['email'] = message.text
        bot.send_message(message.chat.id, "Отлично! Теперь отправьте ваш пароль.")
    elif user_data['password'] is None:
        user_data['password'] = message.text
        bot.send_message(message.chat.id, "Спасибо! Ваши данные сохранены.")

        # Отправляем пользователю сохраненные данные
        response_message = f"Ваши данные:\nE-mail: {user_data['email']}\nPassword: {user_data['password']}\n ChatId: {user_data['chatId']}"
        bot.send_message(message.chat.id, response_message)
        print (data_list_user[0])
        response = requests.post(f"{server_url1}{notify_endpoint1}", json=data_list_user[0])

        if response.status_code == 201:
            print("Data sent to server successfully")
            bot.send_message(chat_id=message.chat.id, text= "Вы успешно прошли авторизацию. Теперь уведомления о статусе"
                                                            " Ваших товаров будут приходить не только в личный кабинет "
                                                            "<b>td-market</b>, но и в этот чат. Рекомендуем не выключать уведомления "
                                                            "что бы не пропустить новые уведомления)", reply_markup= finish())
            data_list_user.clear()
            bot.delete_state(message.from_user.id, message.chat.id)

        else:
            print(f"Error sending data: {response.status_code}")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.row_width = 1
            keyboard.add (types.InlineKeyboardButton(text='Регистрация на сайте', url='https://td-market.md/'),
                          types.InlineKeyboardButton(text="Поробовать еще раз",callback_data="notification"))
            bot.send_message(chat_id=message.chat.id,text="Вы ввели неверный логин или пароль, попробуйте ввести данные"
                                                          "еще раз или пройдите регистрацию на сайте по ссылке ниже.",
                             reply_markup=keyboard)
            data_list_user.pop(0)
            bot.delete_state(message.from_user.id, message.chat.id)
