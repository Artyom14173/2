import sqlite3, sys

class Phonebook(object):
    def __init__(self):
        try:
            c.execute('CREATE TABLE entries(id INTEGER PRIMARY KEY, name TEXT, phone TEXT unique)')
        except:
            pass
        print('Welcome to the Phonebook')

    def addEntry():
        name = input('Введите имя: ')
        number = input('Введите номер телефона: ')
        c.execute('INSERT INTO entries(name, phone) VALUES(?,?)', (name, number))

    def delEntry():
        name = input('Please, enter a name to delete: ')
        c.execute('DELETE FROM entries WHERE name=?', [name])

    def rollback():
        db.rollback()

    def save():
        db.commit()
    
    def query():
        c.execute('SELECT name, phone FROM entries')
        for items in c:
            print(items)

class MainMenu(Phonebook):
    def __init__(self):
        print('''
Меню
Выберите действие:
    1. "добавить" - добавить контакт.
    2. "удалить" - удалить контакт.
    3. "отменить" - отменить последнее действиеe.
    4. "сохранить" - сохранить изменения.
    5. "список" - посмотреть список.
            ''')

        selection = input()
        if selection == 'добавить':
            try:
                Phonebook.addEntry()
            except IntegrityError:
                print('Телефонный номер добавлен.')

        if selection == 'удалить':
            Phonebook.delEntry()

        if selection == 'отменить':
            Phonebook.rollback()

        if selection == 'сохранить':
            Phonebook.save()
            
        if selection == 'список':
            Phonebook.query()

db = sqlite3.connect('phonebookDB.sqlite')
c = db.cursor()

Phonebook()
while True:
    MainMenu()

db.close()
