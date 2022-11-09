from bs4 import BeautifulSoup, SoupStrainer  # HTML parsing
import urllib.request  # aufrufen von URLs
from time import sleep  # damit legen wir den Scraper schlafen
import json  # lesen und schreiben von JSON-Dateien
from datetime import datetime  # um den Daten Timestamps zu geben
import re  # regular expressions
import os  # Dateipfade erstellen und lesen
import pandas as pd  # Datenanalyse und -manipulation

folders = ["data/visited/", "data/autos/"]
# print(os.getcwd())
# for folder in folders:
#     if not os.path.isdir(folder):
#         os.mkdir(folder)
#         print(os.path, "erstellt.")
#     else:
#         print(folder, "existiert bereits")
#
# path_to_visited_urls = "data/visited/visited_urls.json"
#
#
#
# if not os.path.isfile(path_to_visited_urls):
#     with open(path_to_visited_urls, "w") as file:
#         json.dump([], file)

# full_df = pd.DataFrame()
# auto_dir_path = os.path.join(os.getcwd(), folders[1])#, file)
# for file in os.listdir(auto_dir_path):
#     if file.endswith('.csv'):
#         file_path = os.path.join(auto_dir_path, file)
#         partial_df = pd.read_csv(file_path, on_bad_lines='skip')
#         print(partial_df.shape)
#         # print(os.path.join(auto_dir_path, file))
#         full_df = pd.concat([partial_df, full_df])

df = pd. concat([pd.read_csv("data/autos/" + file, sep=";") for file in os. listdir("data/autos/")],
                 axis=0,
                 sort=True)

df.sort_values(by=["date"],
               axis=0,
               ascending=False,
               inplace=True)

selected_columns = ['url',
                    'type',
                    'price_label',
                    'price',
                    'mark',
                    'location',
                    'date',
                    'country',
                    'car_info',
                    'Erstzulassung',
                    'Kilometerstand',
                    'Zustand',
                    ]