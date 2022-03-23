from aiogram import types
from main import new_parse, parse_gend, price_checker
from loader import dp, bot
import time
import pandas as pd


@dp.message_handler(commands='check')
async def check(message: types.Message):
  cur_price = parse_gend()[1]
  sec = 0
  await message.answer(f"Время: {parse_gend()[0]} \n {parse_gend()[2]} \n Актуальная цена: {parse_gend()[1]}₽ \n Старая цена:{cur_price}₽ \n Разница: {cur_price - parse_gend()[1]}₽")
  while True:
    if cur_price != parse_gend()[1]:
      diff = cur_price - parse_gend()[1]
      msg = f"Время: {parse_gend()[0]} \n {parse_gend()[2]} \n Актуальная цена: {parse_gend()[1]}₽ \n Старая цена:{cur_price}₽ \n Разница: {diff}₽"
      await message.answer(msg)
      cur_price = parse_gend()[1]
      sec = 0
    else:
      sec +=1
      time.sleep(2)
      print(sec)
      if sec == 20:
        await message.answer('я задолбался ждать, хватит')
        break
      continue



@dp.message_handler(commands="check_wp")
async def check_wp(message: types.Message):
  cur_price_wp = new_parse()[2]
  await message.answer(f"Время: {new_parse()[0]} \n {new_parse()[2]} \n Актуальная цена: {new_parse()[1]}₽ \n Старая цена:{cur_price_wp}₽ \n Разница: {cur_price_wp - new_parse()[1]}₽")
  sec = 0
  while True:
    if cur_price_wp != new_parse()[2]:
      msg_new = f"Время: {new_parse()[0]} \n {new_parse()[1]} \n Актуальная цена: {new_parse()[2]}₽ \n Старая цена:{cur_price_wp}₽ \n Разница: {cur_price_wp - new_parse()[2]}₽"
      await message.answer(msg_new)
      cur_price_wp = new_parse()[2]
      sec = 0
    else:
      sec += 1
      time.sleep(2)
      print(sec)
      if sec == 20:
        await message.answer('я задолбался ждать, хватит')
        break
      continue


@dp.message_handler(commands="check_article")
async def check_article(message: types.Message):
    try:
      await bot.send_photo(message.from_user.id, "https://s1.livelib.ru/boocover/1003156338/200/8be5/boocover.jpg")
      data = price_checker()
      await message.answer(f"Название книги: {data[0]}"+\
                           f"\nЦена: {data[1]}")
    except Exception as ex:
      await message.answer(f"Ошибка - {ex}")

