import pyowm
import telebot

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here

owm = OWM('241bdb52c8dfd34d672a79b17351fbd9', config_dict)



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Здравствуй, напиши название города ")


@bot.message_handler(content_types = "text" )
def send_echo(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place( message.text )
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	bot.send_message(message.chat.id, "В городе " + message.text + " сейчас " + w.detailed_status + "\n\n"
		"Температура за окном: " + str(temp) )

bot.polling()	
heroku login