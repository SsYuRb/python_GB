import pandas as pd
import number_creater
import names_creater
import creat_posision

def make_database(count):
    array_of_names = [0]*count 
    array_of_numbers = [0]*count
    for i in range (count):
        array_of_names[i] = names_creater.create_some_name()
        array_of_numbers[i] = number_creater.create_some_numbers()
    dataframe = pd.DataFrame({'имя': array_of_names, 'номер телефона': array_of_numbers, 'должность': creat_posision.pos_maker(''), 'e-mail': ''})
    return dataframe