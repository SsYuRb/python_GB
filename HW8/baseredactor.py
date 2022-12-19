
import pandas as pd

def redactor():
    my_phonebook = pd.read_csv('base_of_data.csv', index_col=0)
    name = input('Введите имя человека, которого хотите изменить: ')
    print ('Введите номер данных, которые хотите изменить: \
        1. Имя, 2. Номер телефона, 3. Должность, 4. Почту')
    chages = int(input ())
    if chages == 1:
        new_name = input ('Введите новое имя для пользователя: ')
        my_phonebook.loc[(my_phonebook['имя'] == name), 'имя'] = new_name
        my_phonebook.to_csv('base_of_data.csv')
        my_phonebook.to_html('base_of_data.html')
    elif chages == 2:
        new_number = input ('Введите новый номер для пользователя: ')
        my_phonebook.loc[(my_phonebook['имя'] == name), 'номер телефона'] = new_number
        my_phonebook.to_csv('base_of_data.csv')
        my_phonebook.to_html('base_of_data.html')
    elif chages == 3:
        new_position = input ('Введите новую должность для пользователя: ')
        my_phonebook.loc[(my_phonebook['имя'] == name), 'должность'] = new_position
        my_phonebook.to_csv('base_of_data.csv')
        my_phonebook.to_html('base_of_data.html')
    elif chages == 4:
        new_mail = input ('Введите новую почту для пользователя: ')
        my_phonebook.loc[(my_phonebook['имя'] == name), 'e-mail'] = new_mail
        my_phonebook.to_csv('base_of_data.csv')
        my_phonebook.to_html('base_of_data.html')