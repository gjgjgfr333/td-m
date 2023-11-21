import time

from telebot import util, types
from telebot.types import InlineKeyboardButton

from inlinekeyboard import finish, ms2
from loader import bot, admin_chat_id, adm_chat
from start import Mystate

@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.callback_staff)
def user_answer(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f'(Покупатель) <b>хочет оформить возврат товара</b>')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)
user_chat_ids=[]

group_chat='-1002061338666'
@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.seller_state)
def user_answer(message):
    global user_chat_ids
    user_chat_id = message.chat.id
    user_chat_ids.append(user_chat_id)
    print (user_chat_ids)
    mk = types.InlineKeyboardMarkup()
    mk.row_width=2
    mk.add(InlineKeyboardButton(text='✅',callback_data='crossmark_yes'),
           InlineKeyboardButton(text='❌',callback_data='crossmark_no'))
    bot.send_message(chat_id=group_chat, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' Выполнил условия кроссмакретинга(наверное)')
    f = bot.forward_message(chat_id=group_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=group_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении суток ваше сообщение будет проверено",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)





@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.first_state)
def user_answer(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' не получил свой заказ в указанный срок.'
                                                 f'Его сообщение')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler( state=Mystate.data_state,content_types=util.content_type_media, chat_types=['private'])
def user_data(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет изменить дату доставки товара.'
                                                 f'Его сообщение')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    time.sleep(10)
    bot.delete_message(chat_id=message.chat.id, message_id=xm.message_id)
    #bot.forward_message(chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)




@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.time_state)
def user_time(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет изменить адресс доставки.'
                                                 f'Его сообщение')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.people_state)
def user_people(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет изменить получателя товара.'
                                                 f'Его сообщение')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.cheep_state)
def user_cheep(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет отменить заказ.'
                                                 f'Его сообщение')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.long_dilevery)
def user_long_dilevery(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет отменить заказ.'
                                                 f'Его сообщение')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении 24 часов с вами свяжется оператор",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.another)
def user_another(message):
    bot.send_message(chat_id=admin_chat_id, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' хочет отменить заказ.'
                                                 f'Его сообщение')
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id=message.from_user.id)))
    f = bot.forward_message(chat_id=adm_chat, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
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

gruop_chat_predlojka='-4042549465'
user_chat_ids2=[]
@bot.message_handler(content_types=util.content_type_media, chat_types=['private'], state=Mystate.my_money)
def user_answer(message):
    global user_chat_ids2
    user_chat_id = message.chat.id
    user_chat_ids2.append(user_chat_id)
    print (user_chat_ids2)
    mk = types.InlineKeyboardMarkup()
    mk.row_width=2
    mk.add(InlineKeyboardButton(text='✅',callback_data='infa_yes'),
           InlineKeyboardButton(text='❌',callback_data='infa_no'))
    bot.send_message(chat_id=gruop_chat_predlojka, text=f'Данный пользователь {message.from_user.first_name}'
                                                 f' преслал предложку')
    f = bot.forward_message(chat_id=gruop_chat_predlojka, from_chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=gruop_chat_predlojka, text='''#id{id}'''.format(id=message.chat.id), reply_to_message_id=f.message_id,
                     reply_markup=mk)
    xm = bot.send_message(chat_id=message.chat.id,
                          text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>, вам скоро ответят)''',
                          reply_to_message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text="В течении суток ваше сообщение будет проверено",
                     reply_markup=finish())
    bot.delete_state(message.from_user.id, message.chat.id)
