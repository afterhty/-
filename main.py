import os

from flask import Flask, request
from telebot import types

import telebot

TOKEN = ''5178549233:AAFzGJ_ilc5yFKMwvRmZYerFeoYOWsQ_KEg'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


#КОД ТЕЛЕБОТА

import telebot # импортируем библиотеку для создания бота
 
name = ''
surname = ''
age = 0
 
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')
 
def get_name(message): #получаем имя
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)
 
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)
 
def get_age(message):
    global age
    age = int(message.text)
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')
 
# запуск





@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://qweyuuiu.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
