from telebot import TeleBot
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StatePickleStorage
from telebot.custom_filters import StateFilter
from loader import TOKEN
ststorage = StatePickleStorage()

bot = TeleBot(state_storage=ststorage, token=TOKEN)