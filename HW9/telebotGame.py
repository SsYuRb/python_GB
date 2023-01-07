
import telebot
from telebot import types
from random import randint, choice
import datetime
import config 
from telegram import Update

quantity = 117
max_grab = 28
game = False
time_now = datetime.datetime.now().time()
 
bot = telebot.TeleBot(config.token())

def handle_game_proc(message):
    global game
    if game and 1 <= int(message.text) <= 28:
        return True
    else:
        return False

    
def handle_game_warning(message):
    global game
    if game and (28 < int(message.text) or int(message.text) < 1):
        return True
    else:
        return False

@bot.message_handler(commands=['start'])
def button(message):
    bot.send_message(message.chat.id, f'Привет ✌️, меня зовут {bot.user.first_name}!')
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Начать игру', callback_data='gameInit')
    item2 = types.InlineKeyboardButton('Узнать время', callback_data='time')
    markup.add(item, item2)
 
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'gameInit':
            bot.send_message(call.message.chat.id, 'Тогда пришло время узнать правила.')
            bot.send_message(call.message.chat.id, 'На столе лежит 117 конфет. Играют два игрока делая ход друг после друга. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardButton("Go", callback_data='1')
            btn2 = types.InlineKeyboardButton("Stop", callback_data='2')
            markup1.add(btn1, btn2)
            msg = bot.send_message(call.message.chat.id,'Нажмите Go, чтобы начать',reply_markup=markup1)
            bot.register_next_step_handler(msg, GoStopHandler)
        elif call.data == 'time':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= f'{str(time_now)[:8]}')
 
@bot.message_handler(content_types=['text'])
def GoStopHandler(message):
    if message.text == 'Go':
        global quantity, max_grab, game
        game = True
        quantity = 117
        bot.reply_to(message, "Начинаем")
        turn = choice(['Bot', 'User'])
        bot.send_message(message.chat.id, f'Начинает {turn}')
        if turn == 'Bot':
            grab = randint(1, max_grab)
            quantity -= grab
            bot.send_message(message.chat.id, f'Бот взял {grab}')
            bot.send_message(message.chat.id, f'Осталось {quantity}')
            bot.send_message(message.chat.id, 'Ход игрока. Сколько конфет взять?')
    elif message.text == 'Stop':
        game = False
        bot.send_message(message.chat.id, 'Остановка игры')

@bot.message_handler(func=handle_game_proc)
def GrabHandler(message):
    global quantity, max_grab, game
    if game: 
        if quantity > 28:
            grab = int(message.text)
            quantity -= grab
            bot.send_message(message.chat.id, f'Осталось {quantity}')
            if quantity > 28:
                grab = randint(1, max_grab)
                quantity -= grab
                bot.send_message(message.chat.id, f'Бот взял {grab}')
                bot.send_message(message.chat.id, f'Осталось {quantity}')
                if quantity > 28:
                    bot.send_message(message.chat.id, 'Ход игрока. Сколько конфет взять?')
                else:
                    bot.send_message(message.chat.id, 'Выиграл пользователь')
                    quantity = 0
                    game = False
            else:
                bot.send_message(message.chat.id, 'Выиграл бот')
                quantity = 0
                game = False
        else:
            bot.send_message(message.chat.id, 'Выиграл пользователь')
            quantity = 0
            game = False


bot.polling()