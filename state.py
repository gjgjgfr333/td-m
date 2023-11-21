from telebot import TeleBot
from telebot.storage import StatePickleStorage
from loader import TOKEN
ststorage = StatePickleStorage()

bot = TeleBot(state_storage=ststorage, token=TOKEN)