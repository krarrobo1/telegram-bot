import math
import os
import telebot

# import nltk.data
# TODO: Load the data for nltk..
# tokenizer = nltk.data.load('tokenizers/punkt/PY3/spanish.pickle')

# Load ENV VARS
from dotenv import load_dotenv, find_dotenv
load_dotenv((find_dotenv()))

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

customers=[]

menu = 	   "1. Margheritha  " \
		   "2. AmericanPizza  " \
		   "3. AmazonicPizza  " \
		   "4. SohoPizza"

def isAskingForPizza(message):
	request = message.text.split()
	if len(request) < 2 or request[1].lower() not in "pizza":
		return False
	else:
		return True

def hasMenu(message):
	if message.chat.id in customers and message.text.isnumeric():
		return True
	else:
		return False

@bot.message_handler(func=isAskingForPizza)
def handle_order(message):

	customers.append(message.chat.id)
	bot.send_message(message.chat.id, "¿Qué desea ordenar? \n" + menu)

@bot.message_handler(func=hasMenu)
def handle_choice(message):
	bot.send_message(message.chat.id, "Buena elección enseguida le preparamos su orden")

@bot.message_handler(commands=['menu'])
def ask_menu(message):
	bot.send_message(message.chat.id, menu)

bot.polling()