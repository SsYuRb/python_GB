import database
import add_contact
import search_number
import pandas as pd

print ('Какую операцию вы хотите выполнить?,' '\n', '0. Сгенерировать рандомный справочник', '\n' ,'1. Найти контакт по базе', '\n', '2. Добавить новый контакт', '\n', 'Выберите соответствующий номер операции: ')
k = int(input())
if k == 0: 
    size_of_book = int(input('Какое количество людей в вашей книжке? '))
    my_phonebook = database.make_database(size_of_book)
    my_phonebook.to_csv('phonebook.csv')
    my_phonebook.to_html('phonebook.html')
elif k == 2:
    my_phonebook = pd.read_csv('phonebook.csv', index_col=0)
    name = input('Введите имя вашего нового контакта: ')
    number = input('Введите номер контакта: ')
    my_phonebook = add_contact.add_new_contact(my_phonebook, name, number)
    my_phonebook.to_csv('phonebook.csv')
    my_phonebook.to_html('phonebook.html')
elif k == 1: 
    my_phonebook = pd.read_csv('phonebook.csv', index_col=0)
    found_cont = input('Введите имя контакта, которого хотите найти: ')
    print (search_number.searcher(my_phonebook, found_cont))