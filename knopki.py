from telebot import types

# Главное меню
def main_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Конвертировать валюту💵')
    but2 = types.KeyboardButton('Узнать курс валют🏦')
    kb.add(but1, but2)
    return kb


# Кнопки валют
def offer_buttons():
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(
        types.InlineKeyboardButton(text='Евро💶', callback_data='euro'),
        types.InlineKeyboardButton(text='Доллар💵', callback_data='dollar'),
        types.InlineKeyboardButton(text='Рубль💴', callback_data='ruble')
    )
    return kb

# кнопки для просмотра курсов
def check_cur():
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(
        types.InlineKeyboardButton(text='Евро💶', callback_data='check_euro'),
        types.InlineKeyboardButton(text='Доллар💵', callback_data='check_dollar'),
        types.InlineKeyboardButton(text='Рубль💴', callback_data='check_ruble')
    )
    return kb

# кнопка назад
def back():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Назад🔙')
    kb.add(but1)
    return kb