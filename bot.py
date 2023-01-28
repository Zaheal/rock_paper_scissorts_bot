from aiogram import Bot, Dispatcher, executor
from configs import load_config
from handlers import process_start_answer


config = load_config('.env')

bot: Bot = Bot(token=config.token)
dp: Dispatcher = Dispatcher(bot)


dp.register_message_handler(process_start_answer, commands='start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)