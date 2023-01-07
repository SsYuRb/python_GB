import telebot, config
import req
import pandas as pd
from telebot import types

bot = telebot.TeleBot(config.token())



@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который показывает курс валют по отношению к рублю')
    bot.send_message(message.chat.id, 'Я могу вывести курсы 34 мировых валют')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btm1 = types.KeyboardButton('Доллар США')
    btm2 = types.KeyboardButton('Евро')
    btm3 = types.KeyboardButton('Китайских юаней')
    markup.add(btm1, btm2, btm3)
    bot.send_message(message.chat.id,'Выбери одну из кнопок, или напиши название другой валюты',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def search(message):
    req.rates()
    df = pd.read_csv('/Users/estaban/Desktop/Прогерство/python_GB/hw10/rates.csv')
    k_fold = message.text
    lk = df.loc[df['Валюта'] == k_fold]
    list1 = str(lk).split()[-1]
    bot.send_message(message.chat.id, f'{list1}')

bot.polling(none_stop=True)