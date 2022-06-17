import telebot
from telebot import TeleBot
from telebot import types

API_TOKEN = '5412866218:AAFKCwkuR7qFd0Qr9TbeunPYY5CbAxUPeWU'
bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    global msg

    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_btn1 = types.KeyboardButton('a')
    item_btn2 = types.KeyboardButton('v')
    item_btn3 = types.KeyboardButton('d')
    markup.add(item_btn1, item_btn2, item_btn3)
    bot.send_message(message.chat.id, "interactive bot v 0.1", reply_markup=markup)

    msg = bot.send_message(message.chat.id, "Hello, enter any text.")
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    try:
        bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=message.text)
    except telebot.apihelper.ApiTelegramException:
        pass
    bot.delete_message(message.chat.id, message.message_id)


bot.infinity_polling()
