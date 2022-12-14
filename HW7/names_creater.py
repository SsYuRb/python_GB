
from mimesis import Person

def create_some_name():
    user = Person('ru')
    return user.full_name()