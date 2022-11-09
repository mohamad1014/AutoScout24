
TYPES = ['Usato', 'Nuovo', 'KM 0', 'Noleggio']

customers = [
    {
        "requester": "Mohamad",
        "email": "mo7amad.al.7ajj@gmail.com",
        "marca": "Fiat",
        "model": None,
        "year_start": None,
        "year_end": None,
        "year_specific": None,
        "cities": ["RM", "TO"],
        "min_price": 100,
        "max_price": None,
        "type": TYPES[0]

    }
    ,
    {
        "requester": "Mohamad",
        "email": "mo7amad.al.7ajj@gmail.com",
        "marca": "Fiat",
        "model": None,
        "year_start": None,
        "year_end": None,
        "year_specific": None,
        "cities": ["RM", "TO"],
        "min_price": 100,
        "max_price": None,
        "type": TYPES[0]

    }
]


def check_year(start=None, end=None, specific=None, registration=None):
    if start:
        if end:
            if [True for x in range(start, end+1) if str(x) in registration]:
                return True
        else:
            if [True for x in range(start, 2023) if str(x) in registration]:
                return True
    if end and not start:
        if [True for x in range(1940, end + 1) if str(x) in registration]:
            return True
    if str(specific) in registration:
        return True
    return False


def check_location(city_codes, location):
    for city_code in city_codes:
        if city_code in location:
            return True
    return False


def check_marca(marca_chosen, marca):
    if marca_chosen.lower() == marca.lower():
        return True
    return False


def check_modello(model_chosen, model):
    if model_chosen.lower() == model.lower():
        return True
    return False


def check_price(max_price, min_price, price):
    if max_price:
        if max_price >= float(price) >= min_price:
            return True
    return False


def check_type(type_wanted, type):
    if type_wanted.lower() == type.lower():
        return True
    return False


def check_row(requester: dict, row):
    url = row['url']
    email = requester['email']

    if any([requester["year_start"], requester["year_end"], requester["year_specific"]]):
        if not check_year(start=requester["year_start"],
                          end=requester["year_end"],
                          specific=requester["year_specific"],
                          registration=row['Immatricolazione']):
            return row['Immatricolazione'], email, url

    if requester['max_price']:
        if not check_price(max_price=requester['max_price'], min_price=requester['min_price'], price=row['price']):
            return row['price'], email, url

    if requester['type']:
        if not check_type(type_wanted=requester['type'], type=row['Tipologia']):
            return row['Tipologia'], email, url

    if requester['marca']:
        if not check_marca(marca_chosen=requester['marca'], marca=row['Marca']):
            return row['Marca'], email, url

    if requester['model']:
        if not check_modello(model_chosen=requester['marca'], model=row['Modello']):
            return row['Modello'], email, url

    if requester['cities']:
        if not check_location(city_codes=requester['cities'], location=row['location']):
            return row['location'], email, url
    return True, email, url
