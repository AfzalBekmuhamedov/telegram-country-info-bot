import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from countryinfo import countryinfo, CountryInfo
load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def commands(message:Message):
    chat_id = message.chat.id
    if message.text == "/start":
        bot.send_message(chat_id,f"Hello! {message.from_user.full_name}",reply_markup=button())
    else:
        bot.send_message(chat_id,f"What kind of help you need?")

def button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = KeyboardButton("country")
    markup.add(keyboard)
    return markup

@bot.message_handler(regexp="country")
def choose_country(message:Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,"Enter the name of the country",reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg,country_info)

def country_info(message:Message):
    chat_id = message.chat.id
    country = message.text
    try:
        data = CountryInfo(country).info()
        name = data["name"]
        capital = data["capital"]
        area = data["area"]
        population = data["population"]
        wiki = data["wiki"]
        bot.send_message(chat_id,f"Country: {name}\nCapital: {capital}\Area: {area} km/kv\nPopulation: {population} people\nSource: {wiki}",reply_markup=button())
    except:
        bot.send_message(chat_id,"An error has been detected")


# if __name__ == "__main__":
#     print("Bot is working")
#     bot.infinity_polling()

