from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
from time import sleep
import json
from datetime import datetime
import re
import os
import pandas as pd
from send_mail import email
from customers import customers, TYPES
from check_row import check_row

folder_dir = "data_automobile_recent/"
#path_to_visited_urls = os.path.join(folder_dir, 'visited_urls.json')
car_counter = 0
loops = 0
country = 'Italie'
multiple_cars_dict = {}
car_URLs = []

path_to_visited_urls = os.path.join(folder_dir, 'visited', 'visited_urls.json')

print(path_to_visited_urls)
# Get the visited urls
while True:
    print(loops)
    loops += 1
    with open(path_to_visited_urls, 'r') as file:
        visited_urls = json.load(file)
        print(f"path to json file:{path_to_visited_urls} with {len(visited_urls)} elements")

    for page in range(1,3):
        try:
            url = f'https://www.automobile.it/usate/page-{page}?b=data&d=DESC'
            only_a_tags = SoupStrainer("a")
            soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml', parse_only=only_a_tags)
        except Exception as e:
            print("Overview: " + str(e) + " " * 50, end="\r")
            pass

        for link in soup.find_all("a", attrs={"class": "jsx-2059509079 Card hover-effect CardAd"}):
            car_URLs.append(link.get("href"))

        car_URLs_unique = [car for car in list(set(car_URLs)) if car not in visited_urls]
        print(f'{country} | Site {page} | {len(car_URLs_unique)} new URLs', end="\r")
    if len(car_URLs_unique) > 0:
        for URL in car_URLs_unique:
            print(f' Auto {car_counter}' + ' ' * 50, end="\r")
            try:
                car_counter += 1
                car_dict= {}
                car_dict["country"] = country
                car_dict["date"] = str(datetime.now())
                car = BeautifulSoup(urllib.request.urlopen('https://www.automobile.it' + URL).read(), 'lxml')
                try:
                    for x in car.find_all("div", attrs={"class": "jsx-3587327592 Item"}):
                        for key, value in zip(
                                x.find_all("span", attrs={"class": "jsx-3587327592 Item__Key font-sm font-regular"}),
                                x.find_all("div", attrs={'class': "jsx-3587327592 Item__Value"})):
                            car_dict[key.text] = value.text

                except Exception as e:
                    print("Exception details:Item Keys " + str(e) + " " * 50 + URL)
                try:
                    car_dict['car_info'] = car.find("h1", attrs={
                        "class": "jsx-2184768976 VipTitle font-regular show-only-desktop"}).text
                except Exception as e:
                    print("Exception details:car_info " + str(e) + " " * 50 + URL)
                try:
                    car_dict['location'] = car.find("p", attrs={
                        "class": "jsx-47552132 SellerSummary__Location"}).text
                except Exception as e:
                    print("Exception details:location " + str(e) + " " * 50 + URL)
                try:
                    car_dict['price'] = "".join(
                        re.findall(r'[0-9]+', car.find("span", attrs={"class": "jsx-139447011 Price"}).text))
                except Exception as e:
                    print("Exception details:price " + str(e) + " " * 50 + URL)

                multiple_cars_dict[URL] = car_dict
                visited_urls.append(URL)
                dict_to_check = car_dict.copy()
                dict_to_check['url'] = 'https://www.automobile.it' + URL
                print(dict_to_check)
                [print(check_row(customer, dict_to_check)) for customer in customers]

            except Exception as e:
                print("Exception details: " + str(e) + " " * 50)
                print('https://www.automobile.it' + URL)
                pass
            print("")
        else:
            print("\U0001F634")
            sleep(2)

    # if len(multiple_cars_dict) > 0:
    #     df = pd.DataFrame(multiple_cars_dict).T
    #     df.to_csv("data_automobile/automobile/" + re.sub("[.,:,-, ]", "_", str(datetime.now())) + ".csv", sep=";", index_label="url")
    # else:
    #     print("No Data")
    # with open(path_to_visited_urls, "w") as file:
    #     json.dump(visited_urls, file)