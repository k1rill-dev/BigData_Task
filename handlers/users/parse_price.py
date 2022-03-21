from aiogram import types
from aiogram.dispatcher import FSMContext
# from main import new_parse, parse_gend
from states.state import StateBot
from loader import dp
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def parse_gend():
  try:
    current_datetime = datetime.now()
    time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    url = 'http://gendalf.cf/'
    r = requests.get(url=url)
    r.encoding = 'utf-8'
    response = r.text
    soup = BeautifulSoup(response, 'lxml')
    body = soup.find('body')
    name = body.find('h1').text
    price = body.find('h2').text.replace('Цена: ', '').replace('₽', '').replace(' ', '')
    return time, int(price), name
  except:
    print('ливай дядя')

def new_parse():
  try:
    current_datetime = datetime.now()
    time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    url = 'http://gendalf.cf:8080/product/игровая-консоль-nintendo-switch-32-gb/'
    r = requests.get(url=url)
    r.encoding = 'utf-8'
    response = r.text
    soup = BeautifulSoup(response, 'lxml')
    name = soup.find('div', class_='summary entry-summary').find('h1').text
    price = soup.find('div', class_='summary entry-summary').find('span', class_='woocommerce-Price-amount amount').find('bdi').text
    return time, name, int(price.split('.')[0])
  except:
    print('ливай дядя')

@dp.message_handler(commands='check')
async def check(message: types.Message):
  cur_price = parse_gend()[1]
  sec = 0
  while True:
    if cur_price != parse_gend()[1]:
      msg = f"Время: {parse_gend()[0]} \n {parse_gend()[2]} \n Актуальная цена: {parse_gend()[1]}₽ \n Старая цена:{cur_price}₽ \n Разница: {cur_price - parse_gend()[1]}₽"
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
