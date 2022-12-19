import basegen
import baseadd
import basesearcher
import baseredactor
import basedel

print ('Какую операцию вы хотите выполнить?,' '\n', '0. Сгенерировать рандомную базу данных', \
        '\n' ,'1. Найти контакт по базе', '\n', '2. Добавить новые данные', \
        '\n', '3. Редактировать контакт', '\n', '4. Удалить контакт', \
        '\n', 'Выберите соответствующий номер операции: ')
k = int(input())
if k == 0: 
    basegen.generate()
elif k == 2:
    baseadd.adder()
elif k == 1: 
    basesearcher.search()
elif k == 3: 
    baseredactor.redactor()
elif k == 4: 
    basedel.deliter()