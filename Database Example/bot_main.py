import telebot
import config
import re
from User import *
from database import insert_varible_into_table

bot = telebot.TeleBot(config.token)
user_dict = {}


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Введите ФИО!')
    bot.register_next_step_handler(msg, name_step)


def name_step(message):
    user = User()
    user.name = message.text
    user_dict[message.chat.id] = user

    msg = bot.send_message(message.chat.id, f'ФИО: {user.name}\n\n'
                                            f'Введите номер телефона!')

    bot.register_next_step_handler(msg, number_step)


def number_step(message):
    valid_number = bool(re.match('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                                 message.text))

    if valid_number is True:
        user = user_dict[message.chat.id]
        user.number = message.text

        msg = bot.send_message(message.chat.id, f'ФИО: {user.name}\n'
                                                f'Номер телефона: {user.number}\n\n'
                                                f'Введите почту!')
        bot.register_next_step_handler(msg, mail_step)
    else:
        msg = bot.send_message(message.chat.id, f'Неверно! Попробуйте заново')
        return


def mail_step(message):
    user = user_dict[message.chat.id]
    user.mail = message.text

    msg = bot.send_message(message.chat.id, f'ФИО: {user.name}\n'
                                            f'Номер телефона: {user.number}\n'
                                            f'Почта: {user.mail}\n\n'
                                            f'Спасибо!')

    insert_varible_into_table(message.chat.id,
                              user.name,
                              user.number,
                              user.mail)


bot.polling()
