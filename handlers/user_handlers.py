import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards_data import create_agree_keyboard, create_game_keyboards
from services import choose_bot, choose_who_won
from lexicon import RU_LEXICON


async def process_start_answer(message: Message):
    await message.answer(RU_LEXICON['/start'], reply_markup=create_agree_keyboard())


async def process_help_answer(message: Message):
    await message.answer(RU_LEXICON['/help'], reply_markup=create_agree_keyboard())


async def process_disagree_answer(message: Message):
    await message.answer('Жаль, конечно, но ты заходи, если что))', reply_markup=ReplyKeyboardRemove())


async def process_agree_answer(message: Message):
    await message.answer('Супер! Выбери, чем ты будешь играть', reply_markup=create_game_keyboards())


async def process_game_answer(message: Message):
    bot_choose: int = choose_bot()
    person_choose: str = message.text
    result: str = choose_who_won(bot_choose=bot_choose, person_choose=person_choose)

    if result == 'win':
        await message.answer(RU_LEXICON['win'], reply_markup=create_agree_keyboard())
    elif result == 'lose':
        await message.answer(RU_LEXICON['lose'], reply_markup=create_agree_keyboard())
    elif result == 'draw':
        await message.answer(RU_LEXICON['draw'], reply_markup=create_agree_keyboard())
    

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_answer, commands='start')
    dp.register_message_handler(process_help_answer, commands='help')
    dp.register_message_handler(process_disagree_answer, text=RU_LEXICON['no'])
    dp.register_message_handler(process_agree_answer, text=RU_LEXICON['yes'])
    dp.register_message_handler(process_game_answer, Text(equals=[RU_LEXICON['rock'],
                                                                RU_LEXICON['paper'],
                                                                RU_LEXICON['scissorts']],
                                                                ignore_case=True))
