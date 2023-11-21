from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def reply():
    rep = types.ReplyKeyboardMarkup(resize_keyboard=True)
    types.KeyboardButton(text="Завершить общение")


def ms2():
    ma2 = InlineKeyboardMarkup()
    ma2.row_width = 1
    ma2.add(InlineKeyboardButton("Ответить", callback_data="call_admin_1")

            )
    return ma2


def msgg():
    ma = InlineKeyboardMarkup()
    ma.row_width = 1
    ma.add(InlineKeyboardButton("Отправить одно сообщение", callback_data="call_1"))
    # InlineKeyboardButton("Начать живое общение", callback_data="call_2"))
    return ma


def wellcome_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text="Получать уведомления от td-market🔔", callback_data="notofication_user"),
               InlineKeyboardButton("Когда будет доставлен мой заказ?🚚", callback_data="order"),
               InlineKeyboardButton("Изменить заказ⚒ ", callback_data="change"),
               InlineKeyboardButton("Отменить заказ🚫", callback_data="delete"),
               InlineKeyboardButton("Статус после оплаты не поменялся🤢", callback_data="statys_dont_change"),
               InlineKeyboardButton("Как мне вернуть заказ?💵", callback_data="pay/callback"),
               InlineKeyboardButton("Я нашел баг🕵🏻‍♀️", callback_data="bag"),
               InlineKeyboardButton("Я не нашел ответа(☹️", callback_data="dont_find_answer"),
               InlineKeyboardButton(text='Для продавца 🧌', callback_data='for_sellers'))
    return markup

def for_sellerss():
    markup9 = InlineKeyboardMarkup()
    markup9.row_width = 1
    markup9.add(InlineKeyboardButton("Стать продавцом🧌", callback_data="seller_create"),
               InlineKeyboardButton("Для сотрудничества(кроссмаркетинг)💰", callback_data="cross_mark"),
               InlineKeyboardButton("Доставка👣", callback_data="seller_dilevery"),
                InlineKeyboardButton(text="Получать уведомления от td-market", callback_data="notification" ),
                InlineKeyboardButton(text="Разместить свой магазин на слайдере🏞️", callback_data="slaider" ),
                InlineKeyboardButton(text="Ваша реклама за наши деньги🎁", callback_data="my_money" ))

    return markup9

def button_for_order():
    mark = InlineKeyboardMarkup()
    mark.row_width = 1
    mark.add(InlineKeyboardButton("Уже оформил🤟", callback_data="issued"),
             InlineKeyboardButton("Срок доставки будущего заказа🧸 ", callback_data="future_order"),
             InlineKeyboardButton("На главную🔙", callback_data="back"))

    return mark


def buttun_dilevery():
    mark1 = InlineKeyboardMarkup()
    mark1.row_width = 1
    mark1.add(InlineKeyboardButton("Хорошо👍🏿", callback_data="good1"),
              InlineKeyboardButton("Не получил заказ в указанный интервал", callback_data="dont_take"),
              #InlineKeyboardButton("Внести изменения в доставку🚗 ", callback_data="change_delivery"),
              InlineKeyboardButton("Назад🔙", callback_data="back_back"))
    return mark1

def kross_marketing():
    key = InlineKeyboardMarkup()
    key.row_width = 1
    key.add(InlineKeyboardButton(text='Выполнено👍',callback_data="for_sellers_yes"),
            InlineKeyboardButton("Назад🔙", callback_data="for_sellers"),
            InlineKeyboardButton("Фоточка📷", callback_data="photochka"))
    return key

def akt_tovara():
    key = InlineKeyboardMarkup()
    key.row_width = 1
    key.add(InlineKeyboardButton(text='Получить АКТ ПРИЕМА-ПЕРЕДАЧИ ТОВАРА',callback_data='akt'),
            InlineKeyboardButton("Назад🔙", callback_data="for_sellers"))
    return key

def url_button():
    key = InlineKeyboardMarkup()
    key.row_width = 1
    key.add(InlineKeyboardButton(text='Перейти на сайт🧞‍♂️',url='https://td-market.md/registration'),
            InlineKeyboardButton("Назад🔙", callback_data="for_sellers"))
    return key

def button_cgange():
    key = InlineKeyboardMarkup()
    key.row_width = 1
    key.add(InlineKeyboardButton("Доставку🚀 ", callback_data="trae"),
            InlineKeyboardButton("На главную🔙", callback_data="back"))

    return key


def button_cgange1():
    key1 = InlineKeyboardMarkup()
    key1.row_width = 1
    key1.add(InlineKeyboardButton("Курьерская📭 ", callback_data="trade1"),
             InlineKeyboardButton("Назад🔙", callback_data="back4"))

    return key1


def buttont():
    keq = InlineKeyboardMarkup()
    keq.row_width = 1
    keq.add(InlineKeyboardButton("Дату доставки", callback_data="data"),
            InlineKeyboardButton("Адрес доставки", callback_data="time"),
            InlineKeyboardButton("Получателя", callback_data="people"),
            InlineKeyboardButton("На главную🔙", callback_data="back"))
    return keq


def button_delete():
    key5 = InlineKeyboardMarkup()
    key5.row_width = 1
    key5.add(InlineKeyboardButton("Один из товаров в заказе больше не нужен✂️ ", callback_data="cut"),
             InlineKeyboardButton("Заказ мне больше не нужен💩", callback_data="no"),
             InlineKeyboardButton("На главную🔙", callback_data="back"))

    return key5


def button_order_not_need():
    key4 = InlineKeyboardMarkup()
    key4.row_width = 1
    key4.add(InlineKeyboardButton("Нашел дешевле🔌", callback_data="cheep"),
             InlineKeyboardButton("Долгая доставка🐌", callback_data="expensive"),
             InlineKeyboardButton("Другая❌", callback_data="another"),
             InlineKeyboardButton("На главную🔙", callback_data="back"))

    return key4


def button_order_cut():
    key3 = InlineKeyboardMarkup()
    key3.row_width = 1
    key3.add(InlineKeyboardButton("Да, так и сделаю♿️", callback_data="good1"),
             InlineKeyboardButton("На главную🔙", callback_data="back"))

    return key3


def buttun_dilevery1():
    mark11 = InlineKeyboardMarkup()
    mark11.row_width = 1
    mark11.add(InlineKeyboardButton("Курьерская доставка🚗 ", callback_data="Express_delivery"),
               InlineKeyboardButton("Назад🔙", callback_data="back_back1"))
    return mark11


def dont_take_order():
    dont = InlineKeyboardMarkup()
    dont.row_width = 1
    dont.add(InlineKeyboardButton("Вчера или ранее", callback_data="Expres_delivery"),
             InlineKeyboardButton("Назад🔙", callback_data="back_back2"))
    return dont


def gen_button():
    button = InlineKeyboardMarkup()
    button.row_width = 1
    button.add(InlineKeyboardButton("Продолжить🧐", callback_data="resume"))
    return button


def good():
    keykey = InlineKeyboardMarkup()
    keykey.row_width = 1
    keykey.add(InlineKeyboardButton("У меня еще есть вопросы🙋🏻‍♀️", callback_data="question"))
    return keykey


def back():
    key0 = InlineKeyboardMarkup()
    key0.row_width = 1
    key0.add(InlineKeyboardButton("На главную🔙", callback_data="back"))

    return key0


def button_pay():
    kes = InlineKeyboardMarkup()
    kes.row_width = 1
    kes.add(InlineKeyboardButton("Хорошо👍🏿", callback_data="good1"),
            InlineKeyboardButton("На главную🔙", callback_data="back"))
    return kes


def finish():
    fish = InlineKeyboardMarkup()
    fish.row_width = 1
    fish.add(InlineKeyboardButton("У меня еще есть вопросы🙋🏻‍♀️", callback_data="question"),
             InlineKeyboardButton("На главную🔙", callback_data="back"))
    return fish
