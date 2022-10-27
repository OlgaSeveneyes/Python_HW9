from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'Выберите действие и введите значения через пробел\n/sum\n/difference\n/multiplication\n/division')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    print (msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def difference_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    print (msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

async def multiplication_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    print (msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def division_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    print (msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')
