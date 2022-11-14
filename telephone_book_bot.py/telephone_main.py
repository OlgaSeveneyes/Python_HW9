import telebot
from telephone_commands import read_file_string
from telephone_commands import search_string

bot = telebot.TeleBot('5413578676:AAEj_tHtCA0fgmW4sS2nPhFue2oeU6uH8f0')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Телефонная книга\n/data - весь список\n/search - поиск контакта')
 
@bot.message_handler(commands=['data'])
def data(message):
    bot.send_message(message.chat.id, read_file_string(message.text))

@bot.message_handler(commands=['searсh'])
def search(message):
    bot.send_message(message.chat.id, 'Введите фамилию для поиска')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, search_string(message.text))

print('yes')
bot.polling()


