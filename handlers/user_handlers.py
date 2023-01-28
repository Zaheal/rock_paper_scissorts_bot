import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aiogram.types import Message, ReplyKeyboardRemove
from keyboards_data import create_agree_keyboard, create_game_keyboards
from services import choose_bot, choose_who_won


async def process_start_answer(message: Message):
    await message.answer('Я предлагаю тебе сыграть в игру "Камень, ножницы, бумага".\n Хочешь?', reply_markup=create_agree_keyboard())


async def process_help_answer(message: Message):
    await message.answer('Я бот, с которым ты можешь сыграть в "Камень, ножницы, бумага". Если ты согласишься, игра начнется.\n\n\
Правила:\nКамень < Бумага < Ножницы. Бумага < Ножницы < Камень. Ножницы < Камень < Бумага.\nНачнем?', reply_markup=create_agree_keyboard())


async def process_disagree_answer(message: Message):
    await message.answer('Жаль, конечно, но ты заходи, если что))', reply_markup=ReplyKeyboardRemove())


async def process_agree_answer(message: Message):
    await message.answer('Супер! Выбери, чем ты будешь играть', reply_markup=create_game_keyboards())


async def process_game_answer(message: Message):
    bot_choose: int = choose_bot()
    person_choose: str = message.text
    result: str = choose_who_won(bot_choose=bot_choose, person_choose=person_choose)

    if result == 'win':
        await message.answer('Ты выиграл. Хочешь ещё?', reply_markup=create_agree_keyboard())
    elif result == 'lose':
        await message.answer('Ты проиграл. Хочешь ещё?', reply_markup=create_agree_keyboard())
    elif result == 'draw':
        await message.answer('Ничья. Хочешь ещё?', reply_markup=create_agree_keyboard())
    
