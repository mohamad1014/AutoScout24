# from bs4 import BeautifulSoup, SoupStrainer  # HTML parsing
# import urllib.request  # aufrufen von URLs
# from time import sleep  # damit legen wir den Scraper schlafen
# import json  # lesen und schreiben von JSON-Dateien
# from datetime import datetime  # um den Daten Timestamps zu geben
# import re  # regular expressions
# import os  # Dateipfade erstellen und lesen
# import pandas as pd  # Datenanalyse und -manipulation
#
# folders = ["data/visited/", "data/autos/"]
# for folder in folders:
#     if not os.path.isdir(folder):
#         os.mkdir(folder)
#         print(os.path, "erstellt.")
#     else:
#         print(folder, "existiert bereits")
#
# path_to_visited_urls = "data/visited/visited_urls.json"
#
# if not os.path.isfile(path_to_visited_urls):
#     with open(path_to_visited_urls, "w") as file:
#         json.dump([], file)
#
# countries = {"Deutschland": "D",
#              "Oesterreich": "A",
#              "Belgien": "B",
#              "Spanien": "E",
#              "Frankreich": "F",
#              "Italien": "I",
#              "Luxemburg": "L",
#              "Niederlande": "NL"}
#
# types = ['Mercedes-Benz', 'Volkswagen', 'BMW', 'Audi', 'Ford', 'Opel', 'Skoda', 'Porsche', 'Toyota', 'Renault', '9ff',
#          'Abarth', 'AC', 'ACM', 'Acura', 'Aiways', 'Aixam', 'Alba-Mobility', 'Alfa-Romeo', 'Alpina', 'Alpine',
#          'Amphicar', 'Angelelli-Automobili', 'Ariel-Motor', 'Artega', 'Aspid', 'Aston-Martin', 'Austin',
#          'Austin-Healey', 'Autobianchi', 'Baic', 'BAIC', 'Bedford', 'Bellier', 'Bentley', 'Boldmen', 'bolloré',
#          'Borgward', 'Brilliance', 'Bristol', 'Bugatti', 'Buick', 'BYD', 'Cadillac', 'Caravans-Wohnm', 'Carver',
#          'Casalini', 'Caterham', 'Changhe', 'Chatenet', 'Chery', 'Chevrolet', 'Chrysler', 'Citroen', 'CityEL',
#          'Corvette', 'Cupra', 'Dacia', 'Daewoo', 'DAF', 'Daihatsu', 'Daimler', 'Dangel', 'De-la-Chapelle', 'De-Tomaso',
#          'Delorean', 'DFSK', 'Dodge', 'Donkervoort', 'DR-Motor', 'DS-Automobiles', 'Dutton', 'e.GO', 'Econelo', 'Edran',
#          'Elaris', 'Embuggy', 'Estrima', 'Evetta', 'EVO', 'Ferrari', 'Fiat', 'FISKER', 'Gac-Gonow', 'Galloper', 'Gappy',
#          'GAZ', 'GEM', 'GEMBALLA', 'Genesis', 'Giana', 'Gillet', 'Giotti-Victoria', 'GMC', 'Goupil', 'Great-Wall',
#          'Grecav', 'Haima', 'Hamann', 'Haval', 'Holden', 'Honda', 'HUMMER', 'Hurtan', 'Hyundai', 'Infiniti',
#          'Innocenti', 'Iso-Rivolta', 'Isuzu', 'Iveco', 'IZH', 'JAC', 'Jaguar', 'Jeep', 'Jensen', 'Karma', 'Kia',
#          'Koenigsegg', 'KTM', 'Lada', 'Lamborghini', 'Lancia', 'Land-Rover', 'LDV', 'LEVC', 'Lexus', 'Lifan', 'Ligier',
#          'Lincoln', 'Linzda', 'Lorinser', 'Lotus', 'Lynk-&-Co', 'Mahindra', 'MAN', 'Mansory', 'Martin', 'Martin-Motors',
#          'Maserati', 'Maxus', 'Maybach', 'Mazda', 'McLaren', 'Mega', 'Melex', 'Mercury', 'MG', 'Microcar', 'Militem',
#          'Minari', 'Minauto', 'MINI', 'Mitsubishi', 'Mitsuoka', 'Morgan', 'Moskvich', 'MP-Lafer', 'MPM-Motors',
#          'Nissan', 'NSU', 'Oldsmobile', 'Oldtimer', 'Pagani', 'Panther-Westwinds', 'Peugeot', 'PGO', 'Piaggio',
#          'Plymouth', 'Polestar', 'Pontiac', 'Proton', 'Puch', 'RAM', 'Regis', 'Reliant', 'Rolls-Royce', 'Rover', 'Ruf',
#          'Saab', 'Santana', 'SEAT', 'Segway', 'Selvo', 'Seres', 'Sevic', 'SGS', 'Shelby', 'Shuanghuan', 'Singer',
#          'smart', 'SpeedArt', 'Spyker', 'SsangYong', 'StreetScooter', 'Studebaker', 'Subaru', 'Suzuki', 'Talbot',
#          'Tasso', 'Tata', 'Tazzari-EV', 'TECHART', 'Tesla', 'Town-Life', 'Trabant', 'trailer-anhänger', 'Triumph',
#          'Trucks-Lkw', 'TVR', 'UAZ', 'Vanden-Plas', 'Vanderhall', 'VAZ', 'VEM', 'VinFast', 'Volvo', 'Wartburg',
#          'Weltmeister', 'Wenckstern', 'Westfield', 'Wiesmann', 'XBus', 'XEV', 'Zastava', 'ZAZ', 'Zhidou', 'Zotye',
#          'Sonstige']
#
#
#
# # countries = {"Deutschland": "D"}
#
# car_counter = 1
# cycle_counter = 0
#
# while True:
#     print(f'Starting ... {datetime.now()}')
#     with open(path_to_visited_urls) as file:
#         visited_urls = json.load(file)
#
#     if len(visited_urls) > 1000000:
#         visited_urls = []
#
#     multiple_cars_dict = {}
#
#     cycle_counter += 1
#
#     for country in countries:
#
#         car_URLs = []
#         page = 1
#         # for page in range(1, 20):
#         for type in types:
#             try:
#                 # url = 'https://www.autoscout24.de/lst?sort=age&desc=1&ustate=N%2CU&size=20&page=' + str(
#                 #     page) + '&cy=' + countries[country] + '&atype=C&'
#                 # 'https://www.autoscout24.de/lst/trailer-anh%C3%A4nger?sort=age&desc=1&ustate=N%2\
#                 # CU&atype=C&cy=D&ocs_listing=include&page=2&search_id=14r7apqpuko'
#
#                 url = 'https://www.autoscout24.de/lst/'+str(type)+'?sort=age&desc=1&atype=C&ustate=N&page=' +str(
#                 page) + '&cy=' + countries[country]
#                 print(url)
#                 only_a_tags = SoupStrainer("a")
#                 soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml', parse_only=only_a_tags)
#             except Exception as e:
#                 print("Overview: " + str(e) + " " * 50, end="\r")
#                 pass
#
#             for link in soup.find_all("a"):
#                 if r"/angebote/" in str(link.get("href")):
#                     car_URLs.append(link.get("href"))
#
#             car_URLs_unique = [car for car in list(set(car_URLs)) if car not in visited_urls]
#
#
#
#             print(f'Run {cycle_counter} | {country} | Site {type} | {len(car_URLs_unique)} new URLs', end="\r")
#         print("")
from bs4 import BeautifulSoup, SoupStrainer  # HTML parsing
import urllib.request  # aufrufen von URLs
from time import sleep  # damit legen wir den Scraper schlafen
import json  # lesen und schreiben von JSON-Dateien
from datetime import datetime  # um den Daten Timestamps zu geben
import re  # regular expressions
import os  # Dateipfade erstellen und lesen
import pandas as pd  # Datenanalyse und -manipulation

folders = ["data/visited/", "data/autos/"]
for folder in folders:
    if not os.path.isdir(folder):
        os.mkdir(folder)
        print(os.path, "erstellt.")
    else:
        print(folder, "existiert bereits")

path_to_visited_urls = "data/visited/visited_urls.json"
car_URLs_unique = [0]
if not os.path.isfile(path_to_visited_urls):
    with open(path_to_visited_urls, "w") as file:
        json.dump([], file)

countries = {"Deutschland": "D",
             "Oesterreich": "A",
             "Belgien": "B",
             "Spanien": "E",
             "Frankreich": "F",
             "Italien": "I",
             "Luxemburg": "L",
             "Niederlande": "NL"}

types = ['Mercedes-Benz', 'Volkswagen', 'BMW', 'Audi', 'Ford', 'Opel', 'Skoda', 'Porsche', 'Toyota', 'Renault', '9ff',
         'Abarth', 'AC', 'ACM', 'Acura', 'Aiways', 'Aixam', 'Alba-Mobility', 'Alfa-Romeo', 'Alpina', 'Alpine',
         'Amphicar', 'Angelelli-Automobili', 'Ariel-Motor', 'Artega', 'Aspid', 'Aston-Martin', 'Austin',
         'Austin-Healey', 'Autobianchi', 'Baic', 'BAIC', 'Bedford', 'Bellier', 'Bentley', 'Boldmen', 'bolloré',
         'Borgward', 'Brilliance', 'Bristol', 'Bugatti', 'Buick', 'BYD', 'Cadillac', 'Caravans-Wohnm', 'Carver',
         'Casalini', 'Caterham', 'Changhe', 'Chatenet', 'Chery', 'Chevrolet', 'Chrysler', 'Citroen', 'CityEL',
         'Corvette', 'Cupra', 'Dacia', 'Daewoo', 'DAF', 'Daihatsu', 'Daimler', 'Dangel', 'De-la-Chapelle', 'De-Tomaso',
         'Delorean', 'DFSK', 'Dodge', 'Donkervoort', 'DR-Motor', 'DS-Automobiles', 'Dutton', 'e.GO', 'Econelo', 'Edran',
         'Elaris', 'Embuggy', 'Estrima', 'Evetta', 'EVO', 'Ferrari', 'Fiat', 'FISKER', 'Gac-Gonow', 'Galloper', 'Gappy',
         'GAZ', 'GEM', 'GEMBALLA', 'Genesis', 'Giana', 'Gillet', 'Giotti-Victoria', 'GMC', 'Goupil', 'Great-Wall',
         'Grecav', 'Haima', 'Hamann', 'Haval', 'Holden', 'Honda', 'HUMMER', 'Hurtan', 'Hyundai', 'Infiniti',
         'Innocenti', 'Iso-Rivolta', 'Isuzu', 'Iveco', 'IZH', 'JAC', 'Jaguar', 'Jeep', 'Jensen', 'Karma', 'Kia',
         'Koenigsegg', 'KTM', 'Lada', 'Lamborghini', 'Lancia', 'Land-Rover', 'LDV', 'LEVC', 'Lexus', 'Lifan', 'Ligier',
         'Lincoln', 'Linzda', 'Lorinser', 'Lotus', 'Lynk-&-Co', 'Mahindra', 'MAN', 'Mansory', 'Martin', 'Martin-Motors',
         'Maserati', 'Maxus', 'Maybach', 'Mazda', 'McLaren', 'Mega', 'Melex', 'Mercury', 'MG', 'Microcar', 'Militem',
         'Minari', 'Minauto', 'MINI', 'Mitsubishi', 'Mitsuoka', 'Morgan', 'Moskvich', 'MP-Lafer', 'MPM-Motors',
         'Nissan', 'NSU', 'Oldsmobile', 'Oldtimer', 'Pagani', 'Panther-Westwinds', 'Peugeot', 'PGO', 'Piaggio',
         'Plymouth', 'Polestar', 'Pontiac', 'Proton', 'Puch', 'RAM', 'Regis', 'Reliant', 'Rolls-Royce', 'Rover', 'Ruf',
         'Saab', 'Santana', 'SEAT', 'Segway', 'Selvo', 'Seres', 'Sevic', 'SGS', 'Shelby', 'Shuanghuan', 'Singer',
         'smart', 'SpeedArt', 'Spyker', 'SsangYong', 'StreetScooter', 'Studebaker', 'Subaru', 'Suzuki', 'Talbot',
         'Tasso', 'Tata', 'Tazzari-EV', 'TECHART', 'Tesla', 'Town-Life', 'Trabant', 'trailer-anhänger', 'Triumph',
         'Trucks-Lkw', 'TVR', 'UAZ', 'Vanden-Plas', 'Vanderhall', 'VAZ', 'VEM', 'VinFast', 'Volvo', 'Wartburg',
         'Weltmeister', 'Wenckstern', 'Westfield', 'Wiesmann', 'XBus', 'XEV', 'Zastava', 'ZAZ', 'Zhidou', 'Zotye',
         'Sonstige']



# countries = {"Deutschland": "D"}

car_counter = 1
cycle_counter = 0

while True:
    print(f'Starting ... {datetime.now()}')
    with open(path_to_visited_urls) as file:
        visited_urls = json.load(file)

    if len(visited_urls) > 1000000:
        visited_urls = []

    multiple_cars_dict = {}

    cycle_counter += 1

    for country in countries:

        car_URLs = []
        page = 1
        # for page in range(1, 20):
        for type in types:
            try:
                # url = 'https://www.autoscout24.de/lst?sort=age&desc=1&ustate=N%2CU&size=20&page=' + str(
                #     page) + '&cy=' + countries[country] + '&atype=C&'
                # 'https://www.autoscout24.de/lst/trailer-anh%C3%A4nger?sort=age&desc=1&ustate=N%2\
                # CU&atype=C&cy=D&ocs_listing=include&page=2&search_id=14r7apqpuko'

                url = 'https://www.autoscout24.de/lst/'+str(type)+'?sort=age&desc=1&atype=C&ustate=N%2CU&size=20&page=' +str(
                page) + '&cy=' + countries[country]
                only_a_tags = SoupStrainer("a")
                soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml', parse_only=only_a_tags)
            except Exception as e:
                print("Overview: " + str(e) + " " * 50, end="\r")
                pass
            for link in soup.find_all("a"):
                if r"/angebote/" in str(link.get("href")):
                    car_URLs.append(link.get("href"))
            temp_car_URLs_unique = max(0,len(car_URLs_unique))
            car_URLs_unique = list(set(car_URLs))
            print(url, len(car_URLs_unique) - temp_car_URLs_unique)
            print(f'Run {cycle_counter} | {country} | Site {type} | {len(car_URLs_unique)} new URLs', end="\r")
        print(" ")
        if len(car_URLs_unique) > 0:

            for URL in car_URLs_unique:
                print(f'Run {cycle_counter} | {country} | Auto {car_counter}' + ' ' * 50, end="\r")
                try:
                    car_counter += 1

                    car_dict = {}
                    car_dict["country"] = country
                    car_dict["date"] = str(datetime.now())
                    car = BeautifulSoup(urllib.request.urlopen('https://www.autoscout24.de' + URL).read(), 'lxml')


                    for key, value in zip(car.find_all("dt"), car.find_all("dd")):
                        car_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")
                    # print("\n mark \n")
                    try:
                        car_dict['mark'] = car.find("span", attrs={"class": "StageTitle_boldClassifiedInfo__L7JmO"}).text
                    except Exception as e:
                        print("Exception details:mark " + str(e) + " " * 50+URL)
                    # print("\n type \n")
                    try:
                        car_dict['type'] = car.find("span", attrs={"class": "StageTitle_model__pG_6i StageTitle_boldClassifiedInfo__L7JmO"}).text
                    except Exception as e:
                        print("Exception details:type " + str(e) + " " * 50+URL)
                    # print("\n car_info \n")
                    try:
                        car_dict['car_info'] = car.find("div", attrs={
                        "class": "StageTitle_modelVersion__Rmzgd"}).text
                    except Exception as e:
                        print("Exception details:car_info " + str(e) + " " * 50+URL)
                    # print("\n location \n")
                    try:
                        car_dict['location'] = car.find("a", attrs={
                        "class": "scr-link LocationWithPin_locationItem__pHhCa"}).text
                    except Exception as e:
                        print("Exception details:location " + str(e) + " " * 50+URL)
                    # print("\n price \n")
                    try:
                        car_dict['price'] = "".join(
                        re.findall(r'[0-9]+', car.find("div", attrs={"class": "PriceInfo_styledPriceRow__2fvRD"}).text))
                    except Exception as e:
                        print("Exception details:price " + str(e) + " " * 50+URL)
                    # print("\n price_label \n")

                    try:
                        car_dict['price_label'] = car.find("div", attrs={
                        "class": "Price_subPriceContainer__2WN4n"}).text
                    except Exception as e:
                        print("Exception details:price_label " + str(e) + " " * 50+URL)
                    # print("\n box \n")
                    try:
                        temp = car.find("div", attrs={
                        "class": "VehicleOverview_containerMoreThanFourItems__QgCWJ"})

                        for key, value in zip(temp.find_all("div", attrs={"class": 'VehicleOverview_itemTitle__W0qyv'}),
                                          temp.find_all("div", attrs={"class": 'VehicleOverview_itemText__V1yKT'})):
                            car_dict[key.text] = value.text
                    except Exception as e:
                        print("Exception details:Container " + str(e) + " " * 50+URL)


                    # print("\n here \n")
                    # car_dict["dealer"] = car.find("div", attrs={"class": "cldt-vendor-contact-box",
                    #                                               "data-vendor-type": "dealer"}) != None

                    # print("\n here1 \n")
                    #
                    # car_dict["private"] = car.find("div", attrs={"class": "cldt-vendor-contact-box",
                    #                                             "data-vendor-type": "privateseller"}) != None
                    #
                    # print("\n here2 \n")
                    #
                    # car_dict["location"] = car.find("div", attrs={"class": "sc-grid-col-12",
                    #                                          "data-item-name": "vendor-contact-city"}).text
                    #
                    # print("\n here3 \n")
                    #
                    # # car_dict["price"] = "".join(
                    # #     re.findall(r'[0-9]+', car.find("div", attrs={"class": "cldt-price"}).text))
                    # car_dict["price"] = "".join(
                    #     re.findall(r'[0-9]+', car.find("div", attrs={"class": "PriceInfo_styledPriceRow__2fvRD"}).text))
                    # ausstattung = []
                    #
                    # print("\n here4 \n")
                    #
                    # for i in car.find_all("div", attrs={
                    #     "class": "cldt-equipment-block sc-grid-col-3 sc-grid-col-m-4 sc-grid-col-s-12 sc-pull-left"}):
                    #     for span in i.find_all("span"):
                    #         ausstattung.append(i.text)
                    #
                    # ausstattung2 = []
                    #
                    # print("\n here5 \n")
                    #
                    # for element in list(set(ausstattung)):
                    #     austattung_liste = element.split("\n")
                    #     ausstattung2.extend(austattung_liste)
                    #
                    # print("\n here6 \n")
                    #
                    #
                    # car_dict["ausstattung_liste"] = sorted(list(set(ausstattung2)))

                    multiple_cars_dict[URL] = car_dict
                    visited_urls.append(URL)
                except Exception as e:
                    print("Exception details: " + str(e) + " " * 50)
                    print('https://www.autoscout24.de' + URL)
                    pass
            print("")

        else:
            print("\U0001F634")
            sleep(2)

    if len(multiple_cars_dict) > 0:
        df = pd.DataFrame(multiple_cars_dict).T
        df.to_csv("data/autos/" + re.sub("[.,:,-, ]", "_", str(datetime.now())) + ".csv", sep=";", index_label="url")
    else:
        print("No Data")
    with open("data/visited/visited_urls.json", "w") as file:
        json.dump(visited_urls, file)
    print('done, gonna wait 30 and then go again')
    sleep(30)