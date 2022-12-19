
import pandas as pd
def deliter():
    my_phonebook = pd.read_csv('base_of_data.csv', index_col=0)
    name = input('Введите имя человека, которого хотите удалить: ')
    my_phonebook = my_phonebook.drop(index=my_phonebook.query("имя == @name").index)
    my_phonebook = my_phonebook.reset_index(drop=True)
    my_phonebook.to_csv('base_of_data.csv')
    my_phonebook.to_html('base_of_data.html')