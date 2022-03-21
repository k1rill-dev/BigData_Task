from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("check", "Проверка цены(обычный сайт)"),
            types.BotCommand("check_wp", "Проверка цены(WordPress сайт)"),
            types.BotCommand("kino", "Рейтинг кино"),
        ]
    )
