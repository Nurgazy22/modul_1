from peewee import *


db = PostgresqlDatabase(database='test', user='postgres', password='1', host='localhost')

class House(Model): # модель для таблицы houses
    image = CharField(null=True)
    date = CharField()
    price = CharField()
    currency = CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'houses'



def write_to_db(data): # создает таблицу houses и записывает в нее данные
    with db:
        db.create_tables([House])
        House.create(image=data['image'], date=data['date'], price=data['price'], currency=data['currency'])
        print('Downloading')


