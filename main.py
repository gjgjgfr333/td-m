from telebot import custom_filters, util
from admin import bot
from loader import bot
from start import bot
from answer import bot
from answer_user import bot
from nitification import bot


__all__ = ['bot']
bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(custom_filters.ChatFilter())
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.infinity_polling(skip_pending=True, allowed_updates=util.update_types)
