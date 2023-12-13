import sqlalchemy
db_params = sqlalchemy.URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="Psip2023",
    host="localhost",
    database="postgres",
    port=5433
)
engine=sqlalchemy.create_engine(db_params) 
connection=engine.connect()                     #error
#sql_query_1=sqlalchemy.text("INSERT INTO public.my_table (name) Values ('skrzynski'), ('kepa'), ('oleksy');")
#sql_query_1=sqlalchemy.text("select * from public.my_table;")
#sql_query_1=sqlalchemy.text("DELETE FROM public.my_table WHERE id = 1;")
#sql_query_1=sqlalchemy.text("UPDATE public.my_table SET name='kepa' WHERE name='malinowski';")

def dodaj_uzytkownika(user:str):
    sql_query_1 = sqlalchemy.text(f"INSERT INTO public.my_table(name) VALUES ('{user}');")
    connection.execute(sql_query_1)
    connection.commit()
# dodaj_uzytkownika(
#     user=input()
# )

def usun_uzytkownika(user:str):
    sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name = '{user}';")
    connection.execute(sql_query_1)
    connection.commit()
# usun_uzytkownika(
#     user=input()
# )

def aktualizuj_uzytkownika(user_1:str,user_2:str):
    sql_query_1 = sqlalchemy.text(f"UPDATE public.my_table SET name= '{user_1}' WHERE name = '{user_2}';")
    connection.execute(sql_query_1)
    connection.commit()
# aktualizuj_uzytkownika(
#     user_1=input('na kogo'),
#     user_2=input('kogo')
# )


