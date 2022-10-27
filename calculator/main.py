from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token('5726046151:AAE2TBb8DO_0yE1KEIIFtYrspSgqM_vcjBI').build()

app.add_handler(CommandHandler("menu", menu_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("difference", difference_command))
app.add_handler(CommandHandler("multiplication", multiplication_command))
app.add_handler(CommandHandler("division", division_command))

print('yes')

app.run_polling()
