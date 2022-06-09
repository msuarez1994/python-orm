import email
import peewee
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename='events_card.log')

database = peewee.MySQLDatabase('pythondb', user='root', password='',
                        host='localhost', port=3306)

class User(peewee.Model):
    username = peewee.CharField(max_length=50, unique=True, index=True)
    email = peewee.CharField(max_length=60, null=False)
    active = peewee.BooleanField(default=False)
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = database
        db_table= 'users'


if __name__ == '__main__':

    if User.table_exists():
        User.drop_table()
        logging.info('Tabla eliminada')
        
    User.create_table()
    logging.info('Tabla recreada...')

    # people = [
    #     {'username': 'admin0', 'email': 'msuarezm1994@gmail.com', 'active': True},
    #     {'username': 'admin1', 'email': 'msuarezm1994@gmail.com', 'active': True},
    #     {'username': 'admin2', 'email': 'msuarezm1994@gmail.com', 'active': False},
    #     {'username': 'admin3', 'email': 'msuarezm1994@gmail.com', 'active': True},
    #     {'username': 'admin4', 'email': 'msuarezm1994@gmail.com', 'active': True},
    #     {'username': 'admin5', 'email': 'msuarezm1994@gmail.com', 'active': True},
    #     {'username': 'admin6', 'email': 'msuarezm1994@gmail.com', 'active': True},
    #     {'username': 'admin7', 'email': 'msuarezm1994@gmail.com', 'active': False},
    #     {'username': 'admin8', 'email': 'msuarezm1994@gmail.com', 'active': False},
    #     {'username': 'admin9', 'email': 'msuarezm1994@gmail.com', 'active': False},
    #     {'username': 'admin10', 'email': 'msuarezm1994@gmail.com', 'active': True},
    #     {'username': 'admin11', 'email': 'msuarezm1994@gmail.com', 'active': True}
    # ]

    # usuario = User.insert(people).execute()
    logging.shutdown()