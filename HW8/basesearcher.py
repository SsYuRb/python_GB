
import search_number
import pandas as pd
def search():
    my_phonebook = pd.read_csv('base_of_data.csv', index_col=0)
    found_cont = input('Введите имя контакта, которого хотите найти: ')
    print (search_number.searcher(my_phonebook, found_cont))