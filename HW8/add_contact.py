


def add_new_contact(dataFrame, name, phone_number, posistion, mail):
    phonebook = dataFrame
    concat = {'имя': name, 'номер телефона': phone_number, 'должность': posistion, 'e-mail': mail}
    phonebook = phonebook.append(concat, ignore_index=True)
    return phonebook