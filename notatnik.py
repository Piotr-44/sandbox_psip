import re

from bs4 import BeautifulSoup
import requests
import folium

#pobranie website'a

nazwa_miejscowości = 'Biała_Podlaska'

def get_coordinates_of(city:str)->list[float, float]:
    # pobranie współrzędnych z treści strony internetowej

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text,'html.parser')

    # . ponieważ odwołujemy się do klasy
    # print(response_html_latitude[23:-7])
    # latitude = re.sub("(\<).*?(\>)", repl='', string=response_html_latitude, count=0, flags=0)

    response_html_latitude = response_html.select('.latitude')[1].text
    response_html_latitude = float(response_html_latitude.replace(',','.'))
    response_html_longitude = response_html.select('.longitude')[1].text
    response_html_longitude = float(response_html_longitude.replace(',','.'))

    return [response_html_latitude, response_html_longitude]

#print(get_coordinates_of(nazwa_miejscowości))




#Zwrócić mapę z pinezką odnoszącą się do użytkownika podanego z klawiatury
#Zwrócić mapę z wszystkimi ...
#RYSOWANIE MAPY
city = get_coordinates_of(city='Biała_Podlaska')

map = folium.Map(location=[52.3,21.0], tiles="OpenStreetMap", zoom_start=7)

for item in nazwa_miejscowości:
    folium.Marker(
        location=city,
        popup='GEOINFORMATYKA RZĄDZIII!!!'

    ).add_to(map)

map.save('mapka.html')