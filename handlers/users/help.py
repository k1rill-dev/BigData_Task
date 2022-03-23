from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/check - проверяет товар на изменение цены(работает только при изменении цены)",
            "/check_wp - проверяет Wordpress сайт на изменение цены(работает только при изменении цены)",
            "/check_article - проверяет и выводит данные о книге 'Девушка с татуировкой дракона'",
            "/csv - отправляет данные об изменении цены в csv файл",
            "/kino - рейтинг фильмов(парсинг с Кинопоиска и IMDb; будет долго😅)",
            "/github - ссылка на github-репозиторий сего бота")
    
    await message.answer("\n".join(text))
