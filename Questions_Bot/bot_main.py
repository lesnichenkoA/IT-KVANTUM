import telebot
import config
import User

bot = telebot.TeleBot(config.token)
user_dict = {}


@bot.message_handler(commands=['authorization'])
def sex(message):
    msg = bot.send_message(message.chat.id,
                           'Введите свой пол (м/ж)!')
    bot.register_next_step_handler(msg, phone)


def phone(message):
    user = User.User()
    user.sex = message.text
    user_dict[message.chat.id] = user
    msg = bot.send_message(message.chat.id,
                           f'Ваш пол: {user.sex}!\n\n'
                           f'Введите номер телефона!')
    bot.register_next_step_handler(msg, name)


def name(message):
    user = user_dict[message.chat.id]
    user.phone = message.text
    msg = bot.send_message(message.chat.id,
                           f'Ваш номер телефона: {user.phone}!\n\n'
                           f'Введите ФИО!')
    bot.register_next_step_handler(msg, mail)


def mail(message):
    user = user_dict[message.chat.id]
    user.mail = message.text
    bot.send_message(message.chat.id,
                     f'Ваш пол: {user.sex}\n'
                     f'Ваш номер телефона: {user.phone}\n'
                     f'Ваше ФИО: {user.name}\n'
                     f'Ваша почта: {user.mail}\n')


bot.polling()
