from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
from time import sleep
import json
from datetime import datetime
import re
import os
import pandas as pd

folder_dir = "data/automobile/"
path_to_visited_urls = os.path.join(folder_dir, 'visited_urls.json')
print(path_to_visited_urls)

with open(path_to_visited_urls, 'r') as file:
    visited_urls = json.load(file)
    print(f"path to json file:{path_to_visited_urls} with {len(visited_urls)} elements")


# car_URLs=[]
car_counter = 0
country = 'Italie'
multiple_cars_dict = {}
car_URLs = []

ii=1

for xx in range(11, 502, 10):
    for page in range(ii, xx):

        try:
            url = f'https://www.automobile.it/usate/page-{page}?b=data&d=DESC'
            only_a_tags = SoupStrainer("a")
            soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml', parse_only=only_a_tags)
        except Exception as e:
            print("Overview: " + str(e) + " " * 50, end="\r")
            pass

        for link in soup.find_all("a", attrs={"class": "jsx-2059509079 Card hover-effect CardAd"}):
            # if r"/angebote/" in str(link.get("href")):
            # print(link.get("href"))
            car_URLs.append(link.get("href"))

        car_URLs_unique = [car for car in list(set(car_URLs)) if car not in visited_urls]
        print(f'{country} | Site {page} | {len(car_URLs_unique)} new URLs', end="\r")
    ii = page

    if len(car_URLs_unique) > 0:

        for URL in car_URLs_unique:
            print(f' Auto {car_counter}' + ' ' * 50, end="\r")
            try:
                car_counter += 1

                car_dict = {}
                car_dict["country"] = country
                car_dict["date"] = str(datetime.now())
                car = BeautifulSoup(urllib.request.urlopen('https://www.automobile.it' + URL).read(), 'lxml')

                # for key, value in zip(car.find_all("dt"), car.find_all("dd")):
                #     car_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")
                # print("\n mark \n")
                try:
                    for x in car.find_all("div", attrs={"class": "jsx-3587327592 Item"}):
                        for key, value in zip(
                                x.find_all("span", attrs={"class": "jsx-3587327592 Item__Key font-sm font-regular"}),
                                x.find_all("div", attrs={'class': "jsx-3587327592 Item__Value"})):
                            car_dict[key.text] = value.text

                except Exception as e:
                    print("Exception details:Item Keys " + str(e) + " " * 50 + URL)
                # print("\n type \n")
                # try:
                #     car_dict['type'] = car.find("span", attrs={
                #         "class": "StageTitle_model__pG_6i StageTitle_boldClassifiedInfo__L7JmO"}).text
                # except Exception as e:
                #     print("Exception details:type " + str(e) + " " * 50 + URL)
                # # print("\n car_info \n")
                try:
                    car_dict['car_info'] = car.find("h1", attrs={
                        "class": "jsx-2184768976 VipTitle font-regular show-only-desktop"}).text
                except Exception as e:
                    print("Exception details:car_info " + str(e) + " " * 50 + URL)
                # print("\n location \n")
                try:
                    car_dict['location'] = car.find("p", attrs={
                        "class": "jsx-47552132 SellerSummary__Location"}).text
                except Exception as e:
                    print("Exception details:location " + str(e) + " " * 50 + URL)
                # print("\n price \n")
                try:
                    car_dict['price'] = "".join(
                        re.findall(r'[0-9]+', car.find("span", attrs={"class": "jsx-139447011 Price"}).text))
                except Exception as e:
                    print("Exception details:price " + str(e) + " " * 50 + URL)
                # print("\n price_label \n")

                # try:
                #     car_dict['price_label'] = car.find("div", attrs={
                #         "class": "Price_subPriceContainer__2WN4n"}).text
                # except Exception as e:
                #     print("Exception details:price_label " + str(e) + " " * 50 + URL)
                # # print("\n box \n")
                # try:
                #     temp = car.find("div", attrs={
                #         "class": "VehicleOverview_containerMoreThanFourItems__QgCWJ"})
                #
                #     for key, value in zip(temp.find_all("div", attrs={"class": 'VehicleOverview_itemTitle__W0qyv'}),
                #                           temp.find_all("div", attrs={"class": 'VehicleOverview_itemText__V1yKT'})):
                #         car_dict[key.text] = value.text
                # except Exception as e:
                #     print("Exception details:Container " + str(e) + " " * 50 + URL)

                multiple_cars_dict[URL] = car_dict
                visited_urls.append(URL)
            except Exception as e:
                print("Exception details: " + str(e) + " " * 50)
                print('https://www.automobile.it' + URL)
                pass
            print("")
        else:
            print("\U0001F634")
            sleep(2)

    if len(multiple_cars_dict) > 0:
        df = pd.DataFrame(multiple_cars_dict).T
        df.to_csv("data/automobile/" + re.sub("[.,:,-, ]", "_", str(datetime.now())) + ".csv", sep=";", index_label="url")
    else:
        print("No Data")
    with open(path_to_visited_urls, "w") as file:
        json.dump(visited_urls, file)
    print('done, gonna wait 30 and then go again')
    # sleep(30)

