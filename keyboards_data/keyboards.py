import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon import RU_LEXICON


def create_agree_keyboard():

    buttons = [
        KeyboardButton(RU_LEXICON['yes']),
        KeyboardButton(RU_LEXICON['no'])
    ]

    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    return keyboard


def create_game_keyboards():

    buttons = [
        KeyboardButton(RU_LEXICON['rock']),
        KeyboardButton(RU_LEXICON['scissorts']),
        KeyboardButton(RU_LEXICON['paper'])
    ]

    keybord: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
    keybord.add(*buttons)

    return keybord