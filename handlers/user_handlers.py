from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards_data import create_agree_keyboard, create_game_keyboards
from services import choose_who_won, create_users_db, add_count_game, add_count_win
from lexicon import RU_LEXICON


async def process_start_command(message: Message):
    create_users_db(message)
    await message.answer(RU_LEXICON['/start'], reply_markup=create_agree_keyboard())


async def process_help_command(message: Message):
    await message.answer(RU_LEXICON['/help'], reply_markup=create_agree_keyboard())


async def process_disagree_answer(message: Message):
    await message.answer(RU_LEXICON['disagree'], reply_markup=ReplyKeyboardRemove())


async def process_agree_answer(message: Message):
    add_count_game(message)
    await message.answer(RU_LEXICON['agree'], reply_markup=create_game_keyboards())


async def process_game_answer(message: Message):
    person_choose: str = message.text
    result: str = choose_who_won(person_choose)

    if result == 'win':
        add_count_win(message)
        await message.answer(RU_LEXICON['win'], reply_markup=create_agree_keyboard())
    elif result == 'lose':
        await message.answer(RU_LEXICON['lose'], reply_markup=create_agree_keyboard())
    elif result == 'draw':
        add_count_game(message)
        await message.answer(RU_LEXICON['draw'], reply_markup=create_game_keyboards())
    

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_disagree_answer, text=RU_LEXICON['no'])
    dp.register_message_handler(process_agree_answer, text=RU_LEXICON['yes'])
    dp.register_message_handler(process_game_answer, Text(equals=[RU_LEXICON['rock'],
                                                                RU_LEXICON['paper'],
                                                                RU_LEXICON['scissorts']],
                                                                ignore_case=True))
