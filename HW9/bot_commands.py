from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from game import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!!')

async def help_c(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/sum\n/help')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_c(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    jok = update.message.text
    msg = jok.split()
    x = int(msg[1])
    y = int(msg[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    name = update.effective_user.first_name
    print("ты говно")
    game(name)
