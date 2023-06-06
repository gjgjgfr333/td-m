from telebot.types import CallbackQuery
from start import Mystate

from loader import bot, admin_chat_id
from inlinekeyboard import button_for_order, button_cgange, button_pay, buttun_dilevery, buttun_dilevery1, \
    button_delete, button_order_cut, button_cgange1, buttont, back, wellcome_markup, good, dont_take_order, \
    button_order_not_need, finish, msgg


@bot.callback_query_handler(func=lambda call: True)
def answer(call: CallbackQuery):
    if call.data == "resume":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Подскажите пожалуйста с чем связан ваш вопрос? \n\nВыберите пункт из меню ниже:",
                              reply_markup=wellcome_markup())


    elif call.data == "order":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Один момент, скажите, "
                                                                                             "вы уже оформили заказ "
                                                                                             "или хотите"
                                                                                             "узнать срок доставки "
                                                                                             "будущего заказа?",
                              reply_markup=button_for_order())
    elif call.data == "change":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Хорошо, подскажите, пожалуйста, что именно вы хотели бы "
                                   "изменить?", reply_markup=button_cgange())
    elif call.data == "statys_dont_change":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Чтобы статус операции обновился, иногда нужно время. Пожалуйста, подождите — в "
                                   "течение"
                                   "часа статус изменится и вы сможете отслеживать заказ. Чтобы информация поступила "
                                   "быстрее, обновите приложение 😊\n\n"
                                   "Также проверьте активные заказы в вашем личном кабинете. Если есть аналогичный "
                                   "заказ"
                                   "со статусом «Оплачен», повода для беспокойства нет — оплата прошла по одному "
                                   "заказу,"
                                   "он задублировался и второй скоро автоматически будет отменён. Далее ваш заказ будет"
                                   "обрабатываться в обычном режиме.",
                              reply_markup=button_pay())
    elif call.data == "pay/callback":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Подскажите, пожалуйста, с чем связан ваш вопрос?")
    elif call.data == "bag":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Немогли бы вы выслать фото места, где происходит техническая ошибка и описать, "
                                   "что конкретно не так работает")
        bot.set_state(call.from_user.id, Mystate.bag, call.message.chat.id)
    elif call.data == "dont_find_answer":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Выберите сопособ общения", reply_markup=msgg())

    elif call.data == "back":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Подскажите пожалуйста с чем связан ваш вопрос? \n\nВыберите пункт из меню ниже:"
                              , reply_markup=wellcome_markup())

    elif call.data == "Express_delivery":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Если вы оформили заказ с курьерской доставкой, вы можете просмотреть дату "
                                   "доставки в"
                                   "личном кабинете"
                                   "Вкладка \"Мои Заказы\" \n\n\n В случае, если вы не можете принять курьера в "
                                   "указанный"
                                   "интервал или хотите перенести доставку. Нажмите, пожалуйста, на кнопку  \"Хочу "
                                   "внести"
                                   "изменения в доставку🚗\"",
                              reply_markup=buttun_dilevery())
    elif call.data == "issued":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Хорошо. Подскажите, пожалуйста, какой тип доставки у вас?",
                              reply_markup=buttun_dilevery1())
    elif call.data == "back_back1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Один момент, скажите, вы уже оформили заказ или хотите узнать срок доставки "
                                   "будущего"
                                   "заказа?",
                              reply_markup=button_for_order())
    elif call.data == "good1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Если вдруг будут еще вопросы,  просто нажмите на кнопку.",
                              reply_markup=good())
    elif call.data == "question":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Подскажите пожалуйста с чем связан ваш вопрос? \n\nВыберите пункт из меню ниже:",
                              reply_markup=wellcome_markup())

    elif call.data == "back_back":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Хорошо. Подскажите, пожалуйста, какой тип доставки у вас?",
                              reply_markup=buttun_dilevery1())
    elif call.data == "dont_take":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Уточните, пожалуйста, когда вы должны были получить заказ?",
                              reply_markup=dont_take_order())
    elif call.data == "back_back2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Если вы оформили заказ с курьерской доставкой, вы можете просмотреть дату "
                                   "доставки в"
                                   "личном кабинете"
                                   "Вкладка \"Мои Заказы\" \n\n\n В случае, если вы не можете принять курьера в "
                                   "указанный"
                                   "интервал или хотите перенести доставку. Нажмите, пожалуйста, на кнопку  \"Хочу "
                                   "внести"
                                   "изменения в доставку🚗\"",
                              reply_markup=buttun_dilevery())
    elif call.data == "trae":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Какой тип доставки у вашего заказа?",
                              reply_markup=button_cgange1())
    elif call.data == "trade1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Хорошо, что именно вы хотели бы изменить?",
                              reply_markup=buttont())
    elif call.data == "data":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Напишите, пожалуйста, номер вашего заказа, ваше Имя и Фамилию.")
        bot.set_state(call.from_user.id, Mystate.data_state, call.message.chat.id)
    elif call.data == "time":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="❗️Обращаем ваше внимание, что курьерская доставка осуществляется только в пределах "
                                   "города, где уже есть td-market. \n\n\n"
                                   "Если вы хотите изменить адрес доставки в пределах города  - напишите, пожалуйста, "
                                   "номер вашего заказа, ваше Имя и Фамилию.")
        bot.set_state(call.from_user.id, Mystate.time_state, call.message.chat.id)
    elif call.data == "people":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Подскажите, пожалуйста, номер вашего заказа, ваше Имя и Фамилию.")
        bot.set_state(call.from_user.id, Mystate.people_state, call.message.chat.id)
    elif call.data == "back4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Хорошо, подскажите, пожалуйста, что именно вы хотели бы изменить&",
                              reply_markup=button_cgange())
    elif call.data == "delete":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Скажите, пожалуйста, по какой причине вы хотели бы отменить заказ?",
                              reply_markup=button_delete())
    elif call.data == "cut":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Если в вашем заказе есть один или несколько товаров, которые вам не нужны - вы "
                                   "всегда"
                                   "можете отказаться от них при получении и отменять заказ не нужно "
                                   "будет.\n\n\nСредства"
                                   "вернутся на вашу карту в течение 1-5 рабочих дней.",
                              reply_markup=button_order_cut())
    elif call.data == "no":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Подскажите, пожалуйста, почему вы решили отменить заказ?",
                              reply_markup=button_order_not_need())
    elif call.data == "cheep":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Напишите, пожалуйста, номер вашего заказа, без лишних символов и пробелов.",
                              reply_markup=back())
        bot.send_message(chat_id=admin_chat_id,
                         text=f'Возможен отмен заказа от {call.message.from_user.first_name}, причина -"нашел дешевле"')
        bot.set_state(call.from_user.id, Mystate.cheep_state, call.message.chat.id)

    elif call.data == "expensive":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Напишите, пожалуйста, номер вашего заказа, без лишних символов и пробелов.",
                              reply_markup=back())
        bot.send_message(chat_id=admin_chat_id,
                         text=f'Возможен отмен заказа от {call.message.from_user.first_name}, причина -"долгая '
                              f'доставка" ')
        bot.set_state(call.from_user.id, Mystate.long_dilevery, call.message.chat.id)
    elif call.data == "another":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Напишите, пожалуйста, номер вашего заказа, без лишних символов и пробелов.",
                              reply_markup=back())
        bot.send_message(chat_id=admin_chat_id,
                         text=f'Возможен отмен заказа от {call.message.from_user.first_name}, причина -"другая"')
        bot.set_state(call.from_user.id, Mystate.another, call.message.chat.id)


    elif call.data == "Expres_delivery":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Напишите, пожалуйста, номер вашего заказа,имя и фамилию получателя")
        bot.set_state(user_id=call.from_user.id, state=Mystate.first_state, chat_id=call.message.chat.id)
    elif call.data == "future_order":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Доставка заказа занимает не больше 7 рабочих дней. Но в "
                                   "большинстве случаев мы успеваем доставить заказ за 2 дня. ",
                              reply_markup=finish())
    elif call.data == "call_1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Введите ваше сообщение")
        bot.set_state(call.from_user.id, Mystate.admin_call_1, call.message.chat.id)

    # elif call.data == "call_admin_1":
    #  bot.send_message(chat_id=admin_chat_id, text= "Введите ваше сообщение (Фото,видео,текст)")
    # bot.set_state(call.from_user.id, Mystate.admin_call_1, call.message.chat.id)
