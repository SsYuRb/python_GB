
import add_contact
import pandas as pd
def adder():
    my_phonebook = pd.read_csv('base_of_data.csv', index_col=0)
    name = input('Введите имя человека: ')
    number = input('Введите номер человека: ')
    position = input('Введите должность человека: ')
    mail = input('Введите почту человека: ')
    my_phonebook = add_contact.add_new_contact(my_phonebook, name, number, position, mail)
    my_phonebook.to_csv('base_of_data.csv')
    my_phonebook.to_html('base_of_data.html')