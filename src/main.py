import os
import telebot
from src.markup import ui_keyboard as ui
from src.data import  data_source

# Load ENV VARS
from dotenv import load_dotenv, find_dotenv
load_dotenv((find_dotenv()))

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

# Opcion 1 Ver Menu (Envia todas las pizzas con sus ingredientes, precios y contenido calorico), Tomar Orden, Finalizar pedido o Seguir Pidiendo)
# Controllers

# Start
@bot.message_handler(func=lambda msg: msg.text == 'start', commands=['start'])
def start(message):
	bot.send_message(message.chat.id,data_source['welcome'] , reply_markup=ui.create_keyboard_menu(['Show me the menu', 'Recommend me an option', 'Show me my order']))


# Info
@bot.message_handler(commands=['info', 'help'])
def on_info(message):
    bot.reply_to(message, data_source['info'] + "\n" + "https://i1.sndcdn.com/artworks-000501693894-wnq8jo-t500x500.jpg" )


# Menu
@bot.message_handler(commands=['menu'])
@bot.callback_query_handler(func= lambda  query: query.data == "Show me the menu")
def on_menu(res):
	chat_id = None
	if(hasattr(res, 'message')):
		chat_id = res.message.chat.id
	else:
		chat_id = res.chat.id
	if(chat_id != None):
		pizza_list = data_source.pizza_list
		for item in pizza_list.keys():
			bot.send_message(
				chat_id,
				ui.create_card(item, pizza_list[item]) ,
				reply_markup=ui.create_keyboard_menu(['S', 'M', 'L'])
			)

# Confirm
@bot.callback_query_handler(func= lambda  query: query.data in data_source.size_list)
def handleConfirm(query):
	choice = query.data
	bot.send_message(query.message.chat.id, "Confirm order", reply_markup=ui.create_payment())

@bot.callback_query_handler(func = lambda query: query.data == "Cancel")
def handleCancelarpedido(query):
	bot.send_message(query.message.chat.id, "You've canceled your order, but dont worry use command /start to try again!")


bot.polling()