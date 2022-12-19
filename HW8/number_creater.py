
import random

def create_some_numbers():
    russian_code = '+7'
    array_numbers = [random.randint(0, 9) for _ in range(10)]
    for i in array_numbers:
        russian_code += str(i)
    return russian_code