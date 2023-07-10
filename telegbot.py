import tempfile

import telebot
from skill import *

bot = telebot.TeleBot('5868508351:AAHDjQ1D9uYfxhckwCgJwEBgoq4q3dk3Exw')



@bot.message_handler(content_types=['text', 'document', 'audio'])
def statrt(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'ну привет')
    if message.text == 'картинка':
        file = open('23.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    if message.text == 'прибавь звук':
        bot.send_message(message.chat.id, 'прибавил звук')
        soundup10()
    else:
        bot.send_message(message.from_user.id, 'я не знаю чего ты хочешь')

@bot.message_handler(regexp='прибавить')
def echo_message(message):
    bot.send_message(message.chat.id,'прибавил звук')
    soundup10()




@bot.message_handler(content_types=["text"])
def echo_message_png(message):
    if message.text == 'картинка':
        file = open('23.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.from_user.id, 'я не знаю что ты хочешь')



bot.infinity_polling()

# if __name__ == '__main__':
#     statrt()
