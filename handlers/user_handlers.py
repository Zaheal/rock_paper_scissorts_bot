import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aiogram.types import Message
from keyboards_data import create_agree_keyboard


async def process_start_answer(message: Message):
    await message.answer('Я предлагаю тебе сыграть в игру "Камень, ножницы, бумага".\n Хочешь?', reply_markup=create_agree_keyboard())