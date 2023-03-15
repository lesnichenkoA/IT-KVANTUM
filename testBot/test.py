import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import config

TOKEN = config.token
bot = telebot.TeleBot(TOKEN)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Старт"),
    telebot.types.BotCommand("/help", "Помощь")
])


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!\n\n"
                                      "Ты можешь поздороваться со мной!")


@bot.message_handler(func=lambda message: 'привет' in message.text.lower())
def hi_message(message):
    bot.send_message(message.chat.id, "Привет!")


bot.infinity_polling()
