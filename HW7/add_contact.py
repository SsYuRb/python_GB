
def add_new_contact(dataFrame, name, phone_number):
    phonebook = dataFrame
    concat = {'имя': name, 'номер телефона': phone_number}
    phonebook = phonebook.append(concat, ignore_index=True)
    return phonebook