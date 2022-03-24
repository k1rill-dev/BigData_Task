from datetime import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from fake_useragent import UserAgent
from data.config import *
import pandas as pd

ua = UserAgent()


# options = webdriver.ChromeOptions()
# options.add_argument('text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
# options.add_argument('--no-sandbox')
# options.add_argument('window-size=1400,600')
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument(f'user-agent={ua.random}')
# # options.binary_location = env.str('GOOGLE_CHROME_SHIM')
# wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # wd = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)


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
        price = soup.find('div', class_='summary entry-summary').find('span',
                                                                      class_='woocommerce-Price-amount amount').find(
            'bdi').text
        return time, name, int(price.split('.')[0])
    except:
        print('ливай дядя')


# def parse_imdb(film):
#     wd.get('https://www.imdb.com/')
#     find_textbox = wd.find_element(By.ID, 'suggestion-search')
#     btn = wd.find_element(By.ID, 'suggestion-search-button')
#     find_textbox.send_keys(film)
#     btn.click()
#     href = wd.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a')
#     href.click()
#     wd.implicitly_wait(5)
#     name = wd.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1')
#     rait = wd.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]')
#     return name.text, rait.text

def parse_imdb(film):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70'
    }
    film = film.split()
    req = requests.get(f'https://www.imdb.com/find?q={"+".join(film)}&ref_=nv_sr_sm', headers=headers)
    resp = req.text
    soup = BeautifulSoup(resp, 'lxml')
    href = 'https://www.imdb.com' + soup.find('table', class_='findList').find('tr', class_='findResult odd').find('td',class_='result_text').find('a').get("href")
    print(href)
    if href is not None:
        req_film = requests.get(href, headers=headers)
        soup = BeautifulSoup(req_film.text, 'lxml')
        name = soup.find(attrs={"data-testid": "hero-title-block__title"})
        rait = soup.find(attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"}).find('span', class_='sc-7ab21ed2-1 jGRxWM')
        # print(name.text, rait.text)
        return name.text, rait.text

def parse_kinopoisk(film):
    # никто не верил, что получится запарсить кинопоиск без selenium
    # меня недооценили)
    film = film.split()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70'
    }
    req = requests.get(f'https://www.kinopoisk.ru/index.php?kp_query={"+".join(film)}', headers=headers)
    response = req.text
    soup = BeautifulSoup(response, 'lxml')
    name = soup.find('div', class_='element most_wanted').find('div', class_='info').find('p', class_='name').text
    reit = soup.find('div', class_='element most_wanted').find('div', class_='right').find('div',
                                                                                           class_='rating ratingGreenBG').text
    return name, reit


def price_checker():
    url = 'https://www.ozon.ru/product/devushka-s-tatuirovkoy-drakona-larsson-stig-250059673/?asb=Nagkc2QZl8PFX9CmVJ%252F0xSOdZQuGYKC%252FHEtTtJqD2xI%253D&asb2=rv1KP_Bp3rVq02k96yKDd82QXChnl7SqU7_w8T-w05l_pTiVWlQoeIv_eZLvmfsN&keywords=девушка+с+татуировкой+дракона&sh=sK0lCmxnfg'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70'
    }
    req = requests.get(url, headers=headers)
    response = req.text
    # print(response)
    soup = BeautifulSoup(response, 'lxml')
    name = soup.find('div', class_='k0n k6n k4n').find('h1', class_='k2u').text
    price = soup.find('div', class_='tk1').find('span', class_='kt0 k0t').text.replace('\u2009', '').replace('\xa0', '')
    return name, price


def main():
    film = input()
    print(parse_imdb(film))
    # # print(parse_kinopoisk(film))
    # print(price_checker())


if __name__ == "__main__":
    main()
