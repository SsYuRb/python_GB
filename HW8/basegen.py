
import database
def generate():
    size_of_book = int(input('Какое количество людей в вашей книжке? '))
    my_phonebook = database.make_database(size_of_book)
    my_phonebook.to_csv('base_of_data.csv')
    my_phonebook.to_html('base_of_data.html')