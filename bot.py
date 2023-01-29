from aiogram import Bot, Dispatcher, executor
from configs import load_config
from handlers import register_user_handlers, register_other_handlers


config = load_config('.env')

bot: Bot = Bot(token=config.token)
dp: Dispatcher = Dispatcher(bot)


register_user_handlers(dp=dp)
register_other_handlers(dp=dp)


if __name__ == '__main__':
    executor.start_webhook(dp, skip_updates=True)
