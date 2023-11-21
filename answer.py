import random
import requests
from telebot.types import CallbackQuery
from start import Mystate
from loader import bot, admin_chat_id
from inlinekeyboard import button_for_order, button_cgange, button_pay, buttun_dilevery, buttun_dilevery1, \
    button_delete, button_order_cut, button_cgange1, buttont, back, wellcome_markup, good, dont_take_order, \
    button_order_not_need, finish, msgg, for_sellerss, url_button, kross_marketing, akt_tovara
from  nitification import data_list
from notification__user import data_list_user
from answer_user import user_chat_ids, user_chat_ids2


@bot.callback_query_handler(func=lambda call: True)
def answer(call: CallbackQuery):
    if call.data == "resume":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Подскажите, пожалуйста, с чем связан ваш вопрос? \n\nВыберите пункт из меню ниже:",
                              reply_markup=wellcome_markup())

    elif call.data == "for_sellers":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Выберите пункт который вас"
                                   " интересует из предложенных ниже",
                              reply_markup=for_sellerss())

    elif call.data == "seller_create":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="<b>Для начала продаж на td-market необходимо</b>\n"
                                   "Просто пройти не сложную регистрацию и все, начинай прямо сейчас"
                                   "по ссылке ниже",
                              reply_markup=url_button())

    elif call.data == "cross_mark":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Если вы хотите получить бесплатную подписку на месяц "
                                   "то вы попали по адрессу)\n\n"
                                   "Для того чтобы получить бесплатную подписку на месяц вам необходимо сделать "
                                   "следующее:\n\n"
                                   "1.Опубликовать историю с фото(прилагается ниже)"
                                   "и надписью о том что вы начали продавать на "
                                   "td-market.\n"
                                   "2.Добавить ссылку своего магазина td-market в шапку профиля вашего instagram "
                                   "аккаунта.\n3. Нажать на кнопку \"Выполнено\" и отправить ссылку на свой"
                                   "instagram аккаунт. ",
                              reply_markup=kross_marketing(), )

    elif call.data == "notification":
        data = {'email': None, 'password': None, 'chatId': None}
        data_list.append(data)
        user_data = data_list[-1]
        if user_data['chatId'] is None:
            user_data['chatId'] = str(call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Для получения уведомлений о заказах Ваших товаров пользователями Вам необходимо"
                                   "пройти авторизацию.\n Для этого введите <b>логин</b> от вашего аккаунта td-market")
        bot.set_state(call.from_user.id,Mystate.notification1,call.message.chat.id)

    elif call.data == "notofication_user":
        data = {'email': None, 'password': None, 'chatId': None}
        data_list_user.append(data)
        user_data = data_list_user[-1]
        if user_data['chatId'] is None:
            user_data['chatId'] = str(call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Для получения уведомлений о заказах Ваших товаров пользователями Вам необходимо"
                                   "пройти авторизацию.\n Для этого введите <b>логин</b> от вашего аккаунта td-market")
        bot.set_state(call.from_user.id,Mystate.notification,call.message.chat.id)

    elif call.data == "photochka":
        with open('photo.jpg', 'rb') as file:
            photo = file.read()
        bot.send_photo(chat_id=call.message.chat.id,
                       photo=photo, reply_markup=back())

    elif call.data == "pay/callback":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
        text="Способ возврата товара зависит от способа выбранной Вами доставки.\n\n"
             "Если при оформлении заказа Вы выбрали способ доставки 'Самовывоз', то просто отнесите товар туда откуда вы его"
             " получали, но не позднее 10 дней с момента получения.\n\n"
             "Если при оформлении заказа Вы выбрали способ доставки 'До двери', курьер должен был вручить вам"
             " <b>АКТ ПРИЕМА-ПЕРЕДАЧИ ТОВАРА</b>. В нем указаны данные продавца"
             ", по ним вы сможете связаться с продавцом и вернуть товар.\n\n Если курьер не вручил вам <b>АКТ ПРИЕМА-ПЕРЕДАЧИ ТОВАРА</b>"
             ", то для возврата товара продавцу Вам необходимо написать свое ФИО и номер заказа, после этого Администрация "
             "вышлет Вам все необходимые данные для возврата товара. ")
        bot.set_state(call.from_user.id, Mystate.callback_staff,call.message.chat.id)

    elif call.data == "crossmark_yes":
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(6))
        server_url='https://api.td-market.md/admin/promocode/{random_digits}'
        response = requests.get(f"{server_url}")
        if response.status_code == 200:
            print(f"Error sending data: {response.status_code}")
        else:
            print(f"Error sending data: {response.status_code}")
            print(response)
        xm=bot.send_message(chat_id=call.message.chat.id, text=f'Поздравляем ваши данные прошли проверку администратором,'
                                                    f'вот ваш промо-код:<b>{random_digits}</b>\n\n'
                                                    f'используйте его на странице "Тариф".\n'
                                                    f'Он позволит вам в течение одного месяца реализовывать товары'
                                                    f'на площадке td-market абсолютно бесплатно.\n'
                                                    f'Хорошего вам настроения и удачных продаж)')
        last_message=xm.message_id

        print(user_chat_ids)
        # Прямая пересылка исходного сообщения пользователя в чат админа
        bot.copy_message(chat_id=user_chat_ids[0], from_chat_id=call.message.chat.id, message_id=last_message,reply_markup=
                         finish())
        bot.delete_message(chat_id=call.message.chat.id,message_id=last_message)
        user_chat_ids.pop(0)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "crossmark_no":
        xm=bot.send_message(chat_id=call.message.chat.id, text='<b>Ваши данные не прошли проверку администратором.</b>\n'
                                                               'Проверьте соответствие всех пунктов получения промокода и попробуйте снова.\n'
                                                               "Для того чтобы получить бесплатную подписку на месяц вам необходимо сделать "
                                   "следующее:\n\n"
                                   "1.Опубликовать историю с фото(прилагается ниже)"
                                   "и надписью о том что вы начали продавать на "
                                   "td-market.\n"
                                   "2.Добавить ссылку своего магазина td-market в шапку профиля вашего instagram "
                                   "аккаунта.\n3. Нажать на кнопку \"Выполнено\" и отправить ссылку на свой"
                                   "instagram аккаунт. ")
        last_message=xm.message_id
        bot.copy_message(chat_id=user_chat_ids[0], from_chat_id=call.message.chat.id, message_id=last_message,reply_markup=
                         finish())
        bot.delete_message(chat_id=call.message.chat.id,message_id=last_message)
        user_chat_ids.pop(0)
        print(user_chat_ids)
        bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
    elif call.data == "for_sellers_yes":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='<b>Отпаравьте ссылку на ваш instagram аккаунт</b>, Администрация проверит наличие '
                                   'следующих'
                                   'пунктов:\n\n 1.Опубликовать историю с фото'
                                   "и нажписью о том что вы начали продавать на "
                                   "td-market.\n"
                                   "2.Добавить ссылку своего магазина td-market в шапку профиля вашего instagram "
                                   "аккаунта.\n3. Нажать на кнопку \"Выполнено\" и отправить ссылку на свой"
                                   "instagram аккаокунт.\n\n <b>Если все бутет в порядке, мы вашлим вам промокод"
                                   "для получения бесплатной подписки на месяяц)</b> ")

        bot.set_state(call.from_user.id, Mystate.seller_state, call.message.chat.id)

    elif call.data == "seller_dilevery":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='В маркетплейсе td-market предусмотренно два вида доставки товара:\n\n'
                                   '1. Доставка товара покупателю курьерами td-market.\n2. Доставка товара покупателю '
                                   'силами продавца.\n\n'
                                   'В случае если Вы доставляете товар своими силами, то Вам необходимо вручать '
                                   'покупателю АКТ'
                                   'ПРИЕМА-ПЕРЕДАЧИ ТОВАРА . Он нужен для:\n\n '
                                   '1. Покупатель подтверждает, что Он получил товар и у товара отсутствуют явные '
                                   'видимые дефекты.\n'
                                   '2. В случае, если товар имеет скрытые дефекты, покупатель будет иметь возможность '
                                   'связаться с вами.\n\n'
                                   'В случае если нет подписанного АКТА '
                                   'ПРИЕМА-ПЕРЕДАЧИ ТОВАРА, td-market не сможет удостовериться в выполнении доставки '
                                   'Вами покупателю.\n'
                                   'АКТ ПРИЕМА-ПЕРЕДАЧИ ТОВАРА подписывается в двух экземплярах. Один остаётся у '
                                   'Покупателя, второй остаётся'
                                   'у Продавца.', reply_markup=akt_tovara())

    elif call.data == "akt":
        with open('АКТ.docx', 'rb') as file:
            f = file.read()
        bot.send_document(chat_id=call.message.chat.id, document=f,
                          reply_markup=back())

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
        bot.send_message(chat_id=call.message.chat.id,
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
                                   "Вкладка \"Мои Заказы\"",
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
                              text="Напишите пожалуйста, номер вашего заказа, ваше Имя, Фамилию и дату, когда Вы "
                                   "сможете получить заказ. В ближайшее время с вами свяжется Оператор")
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

    elif call.data == "infa_yes":
        xm = bot.send_message(chat_id=call.message.chat.id, text=f'Поздравляем ваши данные были одобрены администратором'
                                                                 f'. В ближайше время они будут использоваться. Спасибо и хорошего дня) ')
        last_message = xm.message_id

        print(user_chat_ids2)
        # Прямая пересылка исходного сообщения пользователя в чат админа
        bot.copy_message(chat_id=user_chat_ids2[0], from_chat_id=call.message.chat.id, message_id=last_message, reply_markup=
        finish())
        bot.delete_message(chat_id=call.message.chat.id, message_id=last_message)
        user_chat_ids2.pop(0)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "infa_no":
        xm = bot.send_message(chat_id=call.message.chat.id, text='Увы, но Ваши материалы не прошли проверку администратором и не будут использованны на сайте.'
                                                                 'Попробуйте еще раз')
        last_message = xm.message_id
        bot.copy_message(chat_id=user_chat_ids2[0], from_chat_id=call.message.chat.id, message_id=last_message, reply_markup=
        finish())
        bot.delete_message(chat_id=call.message.chat.id, message_id=last_message)
        user_chat_ids2.pop(0)
        print(user_chat_ids2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    elif call.data == "slaider":
        with open('photo2.png', 'rb') as file:
            photo2 = file.read()
        bot.send_photo(chat_id=call.message.chat.id,photo=photo2, caption='Отправьте нам ваше фото для слайдера'
                                                                          'и мы разместим его на главной странице сайта.\n\n'
                                                                          'Параметры фото:')
        bot.set_state(call.from_user.id,Mystate.my_money,call.message.chat.id)

    elif call.data == "my_money":
        with open('photo3.jpg', 'rb') as file:
            photo3 = file.read()
        bot.send_photo(chat_id=call.message.chat.id,photo=photo3, caption='Отправьте нам фото вашей модели на сером фоне и мы сделаем из этого рекламу.\n\n'
                                                                          'Параметры фото:')
        bot.set_state(call.from_user.id,Mystate.my_money,call.message.chat.id)