from aiogram import Bot, Dispatcher, executor
from configs import load_config
from handlers import process_start_answer, process_help_answer, process_disagree_answer, process_agree_answer, process_game_answer
from lexicon import RU_LEXICON
from aiogram.dispatcher.filters import Text


config = load_config('.env')

bot: Bot = Bot(token=config.token)
dp: Dispatcher = Dispatcher(bot)


dp.register_message_handler(process_start_answer, commands='start')
dp.register_message_handler(process_help_answer, commands='help')
dp.register_message_handler(process_disagree_answer, text=RU_LEXICON['no'])
dp.register_message_handler(process_agree_answer, text=RU_LEXICON['yes'])
dp.register_message_handler(process_game_answer, Text(equals=[RU_LEXICON['rock'], RU_LEXICON['paper'], RU_LEXICON['scissorts']], ignore_case=True))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)