from inlinekeyboard import finish, ms2
from loader import bot, admin_chat_id
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
