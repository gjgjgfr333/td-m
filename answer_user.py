import time

from telebot import util, types

from inlinekeyboard import finish, ms2
from loader import bot, admin_chat_id, adm_id, adm_chat
from start import Mystate


@bot.message_handler(content_types=['text'], state=Mystate.first_state)
def user_answer(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' не получил свой заказ в указанный срок.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=['text'], state=Mystate.data_state)
def user_data(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет изменить дату доставки товара.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)

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

    @bot.message_handler(state=Mystate.admin_call_1, content_types=util.content_type_media, chat_types=['private'])
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


@bot.message_handler(content_types=['text'], state=Mystate.time_state)
def user_time(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет изменить адресс доставки.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=['text'], state=Mystate.people_state)
def user_people(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет изменить получателя товара.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=['text'], state=Mystate.cheep_state)
def user_cheep(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет отменить заказ.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=['text'], state=Mystate.long_dilevery)
def user_long_dilevery(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет отменить заказ.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=['text'], state=Mystate.another)
def user_another(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет отменить заказ.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=['photo', 'text', 'voice'], state=Mystate.bag)
def user_bag(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' нашел техническую ошибку.'
                                                 f'Его сообщение')
    bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="Спасибо большое за помощь в выявлении технических ошибок. \n "
                                                   "Мы постараемся исправить ее как можно быстрее",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=Mystate.first_state,content_types=['text', 'photo', 'voice'])
def user_no_answer(message):
    msgg3=bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' не нашел ответа на свой вопрос.'
                                                 f'Его сообщение\n {msgg3.text}',reply_markup=ms2())

    bot.send_message(chat_id=message.chat.id, text="Вам скоро ответят",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)
