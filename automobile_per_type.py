"""
This script is used to get all the marche and modelli urls to be then used to get all the vehicles in get_all_autos.py
"""

import time

from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
from time import sleep
import json
from datetime import datetime
import re
import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

folder_dir = "data/automobile_per_type/"
path_to_marhce_modelli_urls = os.path.join(folder_dir, 'marche_modelli_urls.json')


opts = webdriver.FirefoxOptions()
opts.headless = True

# initial_url = f'https://www.automobile.it/'
initial_url = f'https://www.automobile.it/audi?b=data&d=DESC'
marche_modelli_urls = []
x_path_location_button_click = "/html/body/div[2]/div/div/div/div/div[2]/button[1]"
x_path_cookie_refusal_click = '//*[@id="onetrust-reject-all-handler"]'
x_path_marche = "/html/body/div[1]/main/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/select"
# x_path_marche_popolari = "/html/body/div[1]/main/div[1]/div/div/div[3]/div/form/div[2]/div[1]/div/div/div[2]/select/optgroup[1]"
# x_path_marche_tutte = "/html/body/div[1]/main/div[1]/div/div/div[3]/div/form/div[2]/div[1]/div/div/div[2]/select/optgroup[2]"

x_path_modelli = "/html/body/div[1]/main/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/form/div[1]/div[1]/div/div/div[3]/select"

# x_path_search = "/html/body/div[1]/main/div[1]/div/div/div[3]/div/form/button[1]"
#
# with open(path_to_marhce_modelli_urls, 'r') as file:
#     marche_modelli_urls = json.load(file)
#     print(f"path to json file:{path_to_marhce_modelli_urls} with {len(marche_modelli_urls)} elements")
#
#
#
# marche_modelli_dict = {}
# marche_index = 1
# modelli_index = 0
# marca_selected=""
# modello_selected=""

# try:
#     url = f'https://www.automobile.it/'
#     only_a_tags = SoupStrainer("a")
#     soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml', parse_only=only_a_tags)
# except Exception as e:
#     print("Overview: " + str(e) + " " * 50, end="\r")
#     pass

# Setting up driver
# driver = webdriver.Firefox()  # options=opts)
# driver.get(initial_url)
# sleep(5)
# location_click = driver.find_element(By.XPATH, x_path_location_button_click)
# cookie_click = driver.find_element(By.XPATH, x_path_cookie_refusal_click)
# cookie_click.click()
# location_click.click()
#
# while True:
#
#     # try:
#     #     # Setting up driver
#     #     driver = webdriver.Firefox()#options=opts)
#     #     driver.get(initial_url)
#     #     sleep(5)
#
#     # Select marche
#     marche_select = Select(driver.find_element(By.XPATH, x_path_marche))
#     marche_select.select_by_index(marche_index)
#     marca_selected = marche_select.first_selected_option.text
#
#     try:
#         # Select modelli
#         modelli_select = Select(driver.find_element(By.XPATH, x_path_modelli))
#         modelli_select.select_by_index(modelli_index)
#         modello_selected = modelli_select.first_selected_option.text
#         print(marca_selected, modello_selected)
#     except Exception as e:
#         print("Exception details:"+ str(e) + " " * 50)
#         marche_index += 1
#         modelli_index = 0
#
#     modelli_index += 1
#     # search_click = driver.find_element(By.XPATH, x_path_search)
#     # search_click.click()
#     sleep(2)
#     print(driver.current_url)
#     marche_modelli_urls.append(driver.current_url)
#     print(f"{marca_selected}:{modello_selected}, urls passed so far: {len(marche_modelli_urls)}\n")
# finally:
#     driver.close()
#     # pass
# # select by visible text
# select.select_by_visible_text('Tutte Le Marche')
#
# # select by value
# select.select_by_value('1')

# with open(path_to_marhce_modelli_urls, "w") as file:
#     json.dump(marche_modelli_urls, file)
#     print(f"path to json file:{path_to_marhce_modelli_urls} with {len(marche_modelli_urls)} elements")
