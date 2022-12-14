import database
import add_contact
import search_number
size_of_book = int(input('Какое количество людей в вашей книжке? '))
my_phonebook = database.make_database(size_of_book)
name = input('Введите имя вашего нового контакта: ')
number = input('Введите номер контакта: ')
my_phonebook = add_contact.add_new_contact(my_phonebook, name, number)
found_cont = input('Введите имя контакта, которого хотите найти: ')
print (search_number.searcher(my_phonebook, found_cont))