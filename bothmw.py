# бот-конвертер валют

import telebot
import knopki
import requests
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot('TOKEN')

# Получаем курсы валют
data = requests.get('HTTPS').json()
USD = float(data[0]['Rate'])
EUR = float(data[1]['Rate'])
RUB = float(data[2]['Rate'])


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте!\nЧто вы хотите сделать?',
                     reply_markup=knopki.main_buttons())
    bot.register_next_step_handler(message, offer)


def offer(message):
    if message.text == 'Конвертировать валюту💵':
        bot.send_message(message.chat.id, '⌛',
                         reply_markup=knopki.offer_buttons())
        # убираем старую клавиатуру
        bot.send_message(message.chat.id, "Выберите валюту, которую хотите конвертировать:",
                         reply_markup=ReplyKeyboardRemove())
    elif message.text == 'Узнать курс валют🏦':
        bot.send_message(message.chat.id, "Отлично!", reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, "Выберите нужную вам валюту для конвертации:",
                         reply_markup=knopki.check_cur())


# обработка кнопок валют
@bot.callback_query_handler(func=lambda call: call.data in ['euro', 'dollar', 'ruble'])
def callback_convert(call):
    user_id = call.message.chat.id

    if call.data == 'euro':
        bot.send_message(user_id, 'Введите сумму в сумах для конвертации в евро:')
        bot.register_next_step_handler(call.message, convert_euro, user_id)
    elif call.data == 'dollar':
        bot.send_message(user_id, 'Введите сумму в сумах для конвертации в доллары:')
        bot.register_next_step_handler(call.message, convert_dollar, user_id)
    elif call.data == 'ruble':
        bot.send_message(user_id, 'Введите сумму в сумах для конвертации в рубли:')
        bot.register_next_step_handler(call.message, convert_ruble, user_id)


## конвертация в доллары
def convert_dollar(message, user_id):
    try:
        amount = float(message.text)
        result = amount / USD
        bot.send_message(user_id, f"{amount} сум = {result} $")
    except ValueError:
        bot.send_message(user_id, "Введите числовое значение!")
        bot.register_next_step_handler(message, convert_dollar, user_id)
        return

    bot.send_message(user_id, "Что хотите сделать дальше?", reply_markup=knopki.main_buttons())
    bot.register_next_step_handler(message, offer)


## конвертация в евро
def convert_euro(message, user_id):
    try:
        amount = float(message.text)
        result = (amount / EUR)
        bot.send_message(user_id, f"{amount} сум = {result} €")
    except ValueError:
        bot.send_message(user_id, "Введите числовое значение!")
        bot.register_next_step_handler(message, convert_euro, user_id)
        return

    bot.send_message(user_id, "Что хотите сделать дальше?", reply_markup=knopki.main_buttons())
    bot.register_next_step_handler(message, offer)


## конвертация в рубли
def convert_ruble(message, user_id):
    try:
        amount = float(message.text)
        result = (amount / RUB)
        bot.send_message(user_id, f"{amount} сум = {result} ₽")
    except ValueError:
        bot.send_message(user_id, "Введите числовое значение!")
        bot.register_next_step_handler(message, convert_ruble, user_id)
        return

    bot.send_message(user_id, "Что хотите сделать дальше?", reply_markup=knopki.main_buttons())
    bot.register_next_step_handler(message, offer)


# обработка кнопок просмотра курсов валют
@bot.callback_query_handler(func=lambda call: call.data in ['check_euro', 'check_dollar', 'check_ruble'])
def callback_check_cur(call):
    user_id = call.message.chat.id
    if call.data == 'check_euro':
        bot.send_message(user_id, f"По данным центрального банка РУ, "
                                  f"курс евро составляет {EUR}сум")
    elif call.data == 'check_dollar':
        bot.send_message(user_id, f"По данным центрального банка РУ, "
                                  f"курс доллара составляет {USD}сум")
    elif call.data == 'check_ruble':
        bot.send_message(user_id, f"По данным центрального банка РУ, "
                                  f"курс российского рубля составляет {RUB}сум")
    bot.send_message(user_id, "Это были самые актуальные данные✔️", reply_markup=knopki.back())
    bot.register_next_step_handler(call.message, start)


bot.polling(none_stop=True)
