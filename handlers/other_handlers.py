from aiogram import Dispatcher
from aiogram.types import Message


async def send_answer(message: Message):
    await message.answer('Вы что-то делаете явно не так :(')
  
def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_answer)
