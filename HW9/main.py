from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from spy import *

app = ApplicationBuilder().token("5911002345:AAEt-6oh7bMk0nsborhJroIy4xdCzONlzC4").build()

app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("help", help_c))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_c))
app.add_handler(CommandHandler("game", game))

print('server avalible')
app.run_polling()
