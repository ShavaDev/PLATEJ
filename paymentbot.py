import telebot

bot = telebot.TeleBot('TOKEN')
CLICK_TOKEN = 'TOKEN'


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_invoice(user_id,
                     provider_token=CLICK_TOKEN,
                     title='Подписка на месяц',
                     description='Крутая доставка!',
                     photo_url='HTTPS',
                     photo_width=300,
                     photo_height=300,
                     is_flexible=False,
                     prices=[telebot.types.LabeledPrice(label='Подписка', amount=20000*100)],
                     currency='UZS',
                     invoice_payload='info',
                     start_parameter='sub')

@bot.pre_checkout_query_handler(lambda query: True)
def pre_check(pre_checkout):
    bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def success(message):
    payment = message.successful_payment.invoice_payload
    bot.send_message(message.chat.id, 'Оплата прошла успешно!')
    bot.send_message(message.chat.id, payment)

bot.polling(non_stop=True)


