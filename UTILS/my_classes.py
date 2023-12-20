import requests
class User:
    def __init__(self, city, nick, name, posts):
        self.city = city
        self.nick = nick
        self.name = name
        self.posts = posts

    def pogoda_z(self, miasto: str):
        url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
        return requests.get(url).json()


npc_1 = User(city="Wrocław", nick="pan mateusz", name="Mateusz", posts=777)
npc_2 = User(city="Lublin", nick="kubica", name="Kuba", posts=88)
print(npc_1.city)
print(npc_2.city)

print(npc_1.pogoda_z(npc_1.city))
print(npc_2.pogoda_z(npc_2.city))

