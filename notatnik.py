
import psycopg2 as pcg
import requests
from bs4 import BeautifulSoup
import folium

db_params = pcg.connect(
    user="postgres",
    password="Psip2023",
    host="localhost",
    database="postgres",
    port=5433
)

cursor = db_params.cursor()

# engine=sqlalchemy.create_engine(db_params)
# connection=engine.connect()                     #error
#sql_query_1=sqlalchemy.text("INSERT INTO public.my_table (name) Values ('skrzynski'), ('kepa'), ('oleksy');")
#sql_query_1=sqlalchemy.text("select * from public.my_table;")
#sql_query_1=sqlalchemy.text("DELETE FROM public.my_table WHERE id = 1;")
#sql_query_1=sqlalchemy.text("UPDATE public.my_table SET name='kepa' WHERE name='malinowski';")

def add_user():
    name = input("Podaj imię:  ")
    nick = input("Podaj nick:  ")
    city = input("Podaj miasto:  ")
    posts = input("Podaj liczbę postów:  ")

    # Check if the user with the same nickname already exists
    check_query = f"SELECT * FROM public.tabela_psip WHERE nick = '{nick}';"
    cursor.execute(check_query)
    existing_user = cursor.fetchone()

    if existing_user:
        print("Taki nick już istnieje.")
        add_user()
    else:
        # Insert the new user
        insert_query = f"INSERT INTO public.tabela_psip(city, nick, name, posts) VALUES ('{city}', '{nick}', '{name}', '{posts}');"
        cursor.execute(insert_query)
        db_params.commit()
        print("Użytkownik dodany pomyślnie.")

# add_user()


def remove_user():
    name = input("Podaj imię użytkownika do usunięcia  ")
    sql_query_1 = f" SELECT * FROM public.tabela_psip WHERE name='{name}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    print('0: Usuń wszystkich ')
    print(f'Znaleziono następujących użytkowników: ')

    for numer_uzytkownika, user_to_be_removed in enumerate(query_result):
        print(f'{numer_uzytkownika + 1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz użytkownika do usunięcia: '))  # wynikiem operacji inpunt jest string więc musimy zMIENIĆ go dalej na ineger
    print(numer)
    if numer == 0:
        sql_query_2 = f"DELETE * FROM public.tabela_psip: "
        cursor.execute(sql_query_2)
        db_params.commit()
    else:
        sql_query_2 = f"DELETE FROM public.tabela_psip WHERE id='{query_result[numer-1][0]}';"
        cursor.execute(sql_query_2)
        db_params.commit()

# remove_user()


def show_users_from():
    sql_query_1 = f' SELECT * FROM public.tabela_psip'
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    for row in query_result:
        print(f'Twój znajomy {row[3]} opublikował {row[4]} postów')

# show_users_from()


def update_user():
    nick_of_user = input('Podaj nick uzytkownika do modyfikacji ')
    sql_query_1 = f" SELECT * FROM public.tabela_psip WHERE nick =  '{nick_of_user}';"
    cursor.execute(sql_query_1)
    print('Znaleziono !!!')
    city = input('Podaj nową nazwę miasta: ').strip()
    nick = input('Podaj nowy nick: ').strip()
    name = input('Podaj nowe imię: ').strip()
    posts = int(input('Podaj nową liczbę postów: '))
    sql_query_2 = f"UPDATE public.tabela_psip SET city ='{city}', nick ='{nick}',name ='{name}',posts = '{posts}' WHERE nick = '{nick_of_user}';"
    cursor.execute(sql_query_2)
    db_params.commit()

# update_user()



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



def get_map_one_user():
    city_name = input('Podaj miasto użytkownika: ')
    sql_query_1 = f" SELECT * FROM public.tabela_psip WHERE city ='{city_name}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()

    map = folium.Map(
        location=get_coordinates_of(city_name),
        tiles="OpenStreetMap",
        zoom_start=14
    )
    for user in query_result:
        folium.Marker(
            location=get_coordinates_of(city_name),
            popup=f'Tu rządzi {user[3]}\n'f'Liczba postów: {user[4]} ').add_to(map)
    map.save(f'mapka_{user[1]}_{user[2]}.html')

# get_map_one_user()


def get_map_of():
    map = folium.Map(location=[52.3,21.0], tiles="OpenStreetMap", zoom_start=7)
    sql_query_1 = f" SELECT * FROM public.tabela_psip;"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    for user in query_result:
        folium.Marker(
            location=get_coordinates_of(city=user[1]),
            popup=f'Użytkownik: {user[3]} \n'f'Liczba postów {user[4]}').add_to(map)
    map.save(f'mapka.html')

# get_map_of()


def pogoda_z(miasto: str):
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
    return requests.get(url).json()

# TO DO wlaczyc do kodu aktualnego obsluge baz danych
# TO DO dodac tabele do bazy danych reprezentujaca uzytkownika
# TO DO napisac klase uzytkownika o strukturze zgodnej z ta zdefiniowaną w my_data
# TODO oddac sprawozdanie do dnia 20.12.2023 (sroda)
# TODO MA ZAWIERAC str tytulowa, spis tresci, opis kodu realizojuacego zadanie rysowania mapy uwzgledniajacy poszczegolne funkcje i ich skladnie
# TODO zrealizowany kod na git (link) , podsumowanie wnioski koncowe scy i zdjecia mile widziane