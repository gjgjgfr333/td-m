import telebot
import requests
from telebot import types

# Замените "YOUR_BOT_TOKEN" на ваш токен бота
bot = telebot.TeleBot("6016281493:AAEIcbTY5adYAHn2rA6j2Kl8_KzTMD3iTdw")
server_url = "https://api.td-market.md/auth-shelter"
notify_endpoint = "/check-shelter"
# Создание списка для хранения данных
data_list = []

# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def start(message):
    data = {'email': None, 'password': None}
    data_list.append(data)
    bot.send_message(message.chat.id, "Привет! Пожалуйста, отправьте свой E-mail.")

# Обработчик для текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_messages(message):

    user_data = data_list[-1]  # Получаем последний добавленный элемент списка
    if user_data['email'] is None:
        user_data['email'] = message.text
        bot.send_message(message.chat.id, "Отлично! Теперь отправьте ваш пароль.")
    elif user_data['password'] is None:
        user_data['password'] = message.text
        bot.send_message(message.chat.id, "Спасибо! Ваши данные сохранены.")
        # Отправляем пользователю сохраненные данные
        response_message = f"Ваши данные:\nE-mail: {user_data['email']}\nPassword: {user_data['password']}"
        bot.send_message(message.chat.id, response_message)
        print (data_list[0])
        response = requests.post(f"{server_url}{notify_endpoint}", json=data_list[0])

        if response.status_code == 201:
            print("Data sent to server successfully")
            bot.send_message(chat_id=message.chat.id, text= "Вы успешно прошли авторизацию. Теперь уведомления о покупке"
                                                            "Ваших товаров будут приходить не только в личный кабинет "
                                                            "td-market, но и в этот чат.")
            data_list.clear()

        else:
            print(f"Error sending data: {response.status_code}")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add (types.InlineKeyboardButton(text='Регистрация на сайте', url='https://td-market.md/registration'))
            bot.send_message(chat_id=message.chat.id,text="Вы ввели неверный логин или пароль, попробуйте ввести данные"
                                                          "еще раз или пройдите регистрацию на сайте по ссылке ниже.",
                             reply_markup=keyboard)
            data_list.clear()

# Запуск бота
bot.polling()
