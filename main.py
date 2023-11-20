import threading

from telebot import custom_filters, util
from admin import bot
from loader import bot
from start import bot
from answer import bot
from answer_user import bot
from nitification import bot
from test import bot, send_to_server_thread

@bot.message_handler(func=lambda message: True)
def print_chat_id(message):
    chat_id = message.chat.id
    print(f"Chat ID: {chat_id}")

if __name__ == "__main__":
    # Создание и запуск отдельного потока для функции send_to_server_thread()
    server_thread = threading.Thread(target=send_to_server_thread)
    server_thread.daemon = True  # Установка как демон-потока
    server_thread.start()

__all__ = ['bot']
bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(custom_filters.ChatFilter())
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.infinity_polling(skip_pending=True, allowed_updates=util.update_types)
