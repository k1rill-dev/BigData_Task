from aiogram import types
from aiogram.dispatcher import FSMContext
from states.state import StateBot
from loader import dp
from main import parse_imdb, parse_kinopoisk


@dp.message_handler(commands='kino')
async def check(message: types.Message):
    await message.answer('Введи название фильма(желательно на английском, так как может не найти в IMDb)')
    await StateBot.Kino_ans.set()


@dp.message_handler(state=StateBot.Kino_ans)
async def check_wp(message: types.Message, state: FSMContext):
    try:
        data = parse_imdb(message.text.lower())
        await message.answer(f'Название - {data[0]}' + \
                             f'\nРейтинг IMDb - {data[1]}')
    except Exception:
        await message.answer('Ошибка поиска')

    try:
        data_kp = parse_kinopoisk(message.text.lower())
        await message.answer(f'Название - {data_kp[0]}'+\
                             f'\nРейтинг Кинопоиск - {data_kp[1]}')
    except Exception:
        await message.answer('Ошибка поиска')

    await state.finish()
