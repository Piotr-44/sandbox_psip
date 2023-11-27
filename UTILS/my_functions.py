from bs4 import BeautifulSoup
import requests
import folium
from dane import users_list


#####################################


def add_user_to(users_list:list)-> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imię?')
    posts = input('podaj liczbe postow ?')
    city = input('podaj miasto')
    users_list.append({'name':name, 'posts': posts, 'city': city})



#######################################################


def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list = []
    name = input ('podaj imie uzytkownika do usuniecia?')
    for user in users_list:
        if user["name"]== name:
            tmp_list.append(user)

    print('Znaleziono uzytkownikow:')
    print('0:Usuń wszystkich znalezionych uzytkownikow')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz numer użytkownika do usuniecia: '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])



#################################################



def update_user(users_list: list[dict,dict]) -> None:
    nick_of_user = input('podaj nick uzytkownika do modyfikacji ')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono !!!')
            user['name'] = input('Podaj nowe imie:  ')
            user['nick'] = input('Podaj nowy nick:  ')
            user['posts'] = int(input('Podaj liczbe postow: '))
            user['city'] = input('podaj miasto')


#####################################


def show_users_from(users_list: list)-> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')



#############################################


def get_coordinates_of(city: str) -> list[float, float]:
    # pobranie współrzędnych z treści strony internetowej

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    response_html_latitude = response_html.select('.latitude')[1].text
    response_html_latitude = float(response_html_latitude.replace(',', '.'))
    response_html_longitude = response_html.select('.longitude')[1].text
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]


#####################################


def get_map_one_user(user:str)->None:
    city = get_coordinates_of(user["city"])
    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=14
    )
    folium.Marker(
        location=city,
        popup=f'Tu rządzi {user["name"]},'
              f'Liczba postów: {user["posts"]} '
    ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')


#####################################


def get_map_of(users: list[dict,dict])-> None:
    map = folium.Map(location=[52.3,21.0], tiles="OpenStreetMap", zoom_start=7)

    for user in users:
        folium.Marker(
        location=get_coordinates_of(city=user['city']),
        popup=f'Użytkownik: {user["name"]} \n'
              f'Liczba postów {user["posts"]}'
        ).add_to(map)
    map.save('mapka.html')



def gui(users_list: list) -> None:
    while True:
        print(f' MENU: \n'
              f'0: Zakończ program \n'
              f'1: Wyświetl użytkowników \n'
              f'2: Dodaj użytkownika \n'
              f'3: Usuń użytkownika \n'
              f'4: Modyfikuj użytkowników \n'
              f'5: Wygeneruj mapę z użytkownikiem \n'
              f'6: Wygeneruj mapę z użytkownikami'
              )

        menu_option = input('Podaj funkcję do wywołania ')
        print(f'Wybrano funkcję {menu_option}')

        match menu_option:
            case '0':
                print('kończę pracę')
                break
            case '1':
                show_users_from(users_list)
            case '2':
                print('dodaję użytkownika')
                add_user_to(users_list)
            case '3':
                print('usuwam użytkownika')
                remove_user_from(users_list)
            case '4':
                print('modyfikuję użytkownika')
                update_user(users_list)
            case '5':
                print('Rysuj mape z uzytkownikiem')
                user = input("podaj nazwe uzytkownika")
                for item in users_list:
                    if item['name'] == user:
                        get_map_one_user(item)
            case '6':
                print('Rysuję mapę z wszystkimi użytkownikami')
                get_map_of(users_list)



#gui(users_list)
