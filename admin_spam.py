import json
from loader import adm_id, bot


# обработчик команды /send_all
@bot.message_handler(commands=['send_all'],chat_types=['private'])
def send_to_all(message):
    bot.send_message(chat_id=message.chat.id,text="lox")
    # проверяем, что это администратор бота
    if message.from_user.id == 5988273096:
        # получаем текст сообщения для рассылки
        text = message.text.replace("/send_all", "")
        # открываем файл с данными юзеров
        with open("users.json", "r") as file:
            users = json.load(file)
        # отправляем сообщение каждому юзеру
        for user_id in users:
            bot.send_message(user_id, text)
        bot.reply_to(message, "Рассылка выполнена")
    else:
        bot.reply_to(message, "Вы не администратор")

