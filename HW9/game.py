import time
import random
def game(name1, name2=None, count_candy=117, max_candy_take=28):
    if name2 == None:
        print ('Дорогой друг, против тебя сыграет бот')
    while count_candy != 0:
        winner = 0
        while True: 
            print (f'Игрок {name1} твой ход: ', end = '')
            print ('\r', end='')
            first_pll_choice = int(input())
            while first_pll_choice > max_candy_take or first_pll_choice < 0:
                print (f'Ты можешь взять максимум {max_candy_take} конфет и минимум 1 конфету. {name1} делай новый выбор: ')
                first_pll_choice = int(input())
            winner = name1
            if count_candy - first_pll_choice >= 0:
                print (f'Выбор сделан, конфет осталось: {count_candy-first_pll_choice}')
                count_candy -= first_pll_choice
                break
            else: 
                print ('Ты превысил оставшееся количество')
        if count_candy == 0:
            break
        # if name2 != None: 
        #     while True: 
        #         print (f'Игрок {name2} твой ход: ', end='')
        #         print ('\r', end='')
        #         second_pll_choice = int(input())
        #         while second_pll_choice > max_candy_take or second_pll_choice < 0:
        #             print (f'Ты можешь взять максимум {max_candy_take} конфет и минимум 1 конфету. {name2} сделай новый выбор: ')
        #             second_pll_choice = int(input())
        #         winner = name2
        #         if count_candy - second_pll_choice >= 0:
        #             print (f'Выбор сделан, конфет осталось: {count_candy-second_pll_choice}')
        #             count_candy -= second_pll_choice
        #             break
        #         else: 
        #             print ('Ты превысил оставшееся количество')
        if True: 
            print ('Бот делает свой выбор...', end='')
            time.sleep(1)
            if count_candy > max_candy_take: 
                boot_choice = random.randint(1, max_candy_take)
            else:
                boot_choice = random.randint(1, count_candy)
            print (f'Бот выбрал {boot_choice}')
            winner = 'мистер Бот'
            if count_candy - boot_choice >= 0:
                print (f'Конфет осталось: {count_candy-boot_choice}')
                count_candy -= boot_choice
        if count_candy == 0:
            break
    print (f'Победа за тобой, {winner}')