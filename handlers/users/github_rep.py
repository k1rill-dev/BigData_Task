from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(commands="github")
async def bot_start(message: types.Message):
    await message.answer("Вот ссылка - https://github.com/k1rill-dev/BigData_Task")