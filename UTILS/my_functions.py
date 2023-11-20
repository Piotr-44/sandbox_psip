def add_user_to(users_list:list)-> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imię?')
    posts = input('podaj liczbe postow ?')
    users_list.append({'name':name, 'posts': posts})


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
# remove_user_from(users_list)

# add_user_to(users_list)
# remove_user_from(users_list)
#add_user_to(users_list)
#users_list.remove({"nick":"aaa", "name":"Agata","posts":279})
def update_user(users_list: list[dict,dict]) -> None:
    nick_of_user = input('podaj nick uzytkownika do modyfikacji ')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono !!!')
            user['name'] = input('Podaj nowe imie:  ')
            user['nick'] = input('Podaj nowy nick:  ')
            user['posts'] = int(input('Podaj liczbe postow: '))
def show_users_from(users_list: list)-> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')

#############################################
def gui(users_list: list) -> None:
    while True:
        print(f' MENU: \n'
              f'0: Zakończ program \n'
              f'1: Wyświetl użytkowników \n'
              f'2: Dodaj użytkownika \n'
              f'3: Usuń użytkownika \n'
              f'4: Modyfikuj użytkowników'
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



#gui(users_list)
