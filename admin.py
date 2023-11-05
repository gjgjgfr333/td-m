import json


from telebot import util, types
import time
from loader import bot, adm_chat, adm_id, admin_id_spam
from start import Mystate



@bot.message_handler(commands=['end'])
def bot_off(message):
    bot.send_message(chat_id=message.chat.id, text='бот выключен')
    bot.stop_bot()





# обработчик команды /send_all
@bot.message_handler(commands=['all'])
def send_to_all(message):
    # проверяем, что это администратор бота
    if message.from_user.id == admin_id_spam:
        # получаем текст сообщения для рассылки
        text = message.text.replace("/all ", "")
        # открываем файл с данными юзеров
        with open("users.json", "r") as file:
            users = json.load(file)
        # отправляем сообщение каждому юзеру
        for user_id in users:
            bot.send_message(user_id, text)
        bot.reply_to(message, "Рассылка выполнена")
    else:
        bot.reply_to(message, "Вы не администратор")



@bot.message_handler(commands=['support'],chat_types=['private'])
def support (msg):
    bot.send_message(chat_id=msg.chat.id,text= '''👋 Привет <b><a href="tg://user?id={id}">{name}</a></b>!
🧑‍💻 Это чат <b>связи с администрацией</b>
📛 За <b>флуд и спам</b> или <b>сообщения не по теме</b> - <b><u>БАН НАВСЕГДА</u></b>
<i>❗Сообщения по типу «Привет», «как дела» и другие <b>вопросы не по теме будут игнорироваться! Пишите сразу всё в 
одном сообщении!</b></i>'''.format(name = msg.from_user.first_name, id = msg.from_user.id))





@bot.message_handler(content_types=util.content_type_media, is_reply=True, chat_id=adm_id, chat_types=['private'])
def reply_valid(msg):
    try:
        c = bot.copy_message(chat_id=str(msg.reply_to_message.text)[3:], from_chat_id=adm_chat,
                             message_id=msg.message_id)
        xmm = bot.send_message(chat_id=str(msg.reply_to_message.text)[3:],
                               text='''<b>📩 Пришло <u>новое сообщение</u> от поддержки👆</b>''',
                               reply_to_message_id=c.message_id)
        xm = bot.send_message(chat_id=msg.chat.id,
                              text='''<b>Ваше сообщение было <i>успешно доставлено</i> участнику ✅</b>''',
                              reply_to_message_id=msg.message_id)
        time.sleep(10)
        bot.delete_message(chat_id=str(msg.reply_to_message.text)[3:], message_id=xmm.message_id)
        bot.delete_message(chat_id=adm_chat, message_id=xm.message_id)
    except Exception as err:
        bot.send_message(chat_id=msg.chat.id, reply_to_message_id=msg.message_id,
                         text='''<b>⚠️ Произошла ошибка!</b>''')

@bot.message_handler(content_types=util.content_type_media, is_reply=False, chat_id=adm_id, chat_types=['private'])
def reply_valid(msg):
    xmm = bot.send_message(chat_id=adm_chat,
                           text='''📩 Ответьте на сообщение, <b>в котором есть идентификатор</b> <i><u>переадресованного</u> пользователя</i>.''')
    time.sleep(15)
    bot.delete_message(chat_id=adm_chat, message_id=xmm.message_id)

@bot.message_handler(content_types=util.content_type_service, chat_types=['private'])
def servuce(msg):
    xm = bot.reply_to(chat_id=msg.chat.id, text='''❌ Тип <i>сервисных сообщений</i> <b><u>не поддерживается</u></b>!
<i>📩 Отправьте <b>другое</b></i>.''', reply_to_message_id=msg.message_id)
    time.sleep(15)
    bot.delete_message(chat_id=msg.chat.id, message_id=xm.message_id)
    bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)

@bot.edited_message_handler(content_types=util.content_type_media, chat_types=['private'])
def edit(msg):
    xm = bot.send_message(chat_id=msg.chat.id, text='''✍️ Сообщение уже <b><u>нельзя</u> отредактировать</b>.
<i>📩 Лучше <b>отправьте новое</b></i>.''', reply_to_message_id=msg.message_id)
    time.sleep(15)
    bot.delete_message(chat_id=msg.chat.id, message_id=xm.message_id)

@bot.message_handler(state = Mystate.admin_call_1,content_types=util.content_type_media, chat_types=['private'])
def feedback(msg):

    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=msg.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=msg.chat.id, message_id=msg.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=msg.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=msg.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам
                          скоро ответят)''',
                          reply_to_message_id=msg.message_id)
    time.sleep(10)
    bot.delete_message(chat_id=msg.chat.id, message_id=xm.message_id)
    bot.delete_state(msg.from_user.id, msg.chat.id)












