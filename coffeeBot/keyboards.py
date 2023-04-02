from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def markup_main():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Меню', callback_data='main_menu'))
    markup.add(InlineKeyboardButton('Корзина', callback_data='backet'))
    markup.add(InlineKeyboardButton('Контакты', callback_data='contacts'))

    return markup


def category():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Напитки', callback_data='drinks'))
    markup.add(InlineKeyboardButton('Выпечка', callback_data='bake'))
    markup.add(InlineKeyboardButton('Назад', callback_data='exit'))

    return markup


def list_of_tovars(data, i):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Влево', callback_data=f'switch_{(i - 1) % len(data)}'),
               InlineKeyboardButton('Вправо', callback_data=f'switch_{(i + 1) % len(data)}'))

    markup.add(InlineKeyboardButton('Назад', callback_data='exit'))

    return markup
