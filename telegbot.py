import tempfile

import telebot
from skill import *
from telebot import types
bot = telebot.TeleBot('6307616909:AAFRoF4r1az6rqIuyLYyGOLeK2W19-I-3lk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Прибавь звук")
    btn3 = types.KeyboardButton("Убавь звук")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! ".format(
                         message.from_user), reply_markup=markup)


# def n_v(num_voise):
#     if num_voise in [i for i in range(101)]:
#         return num_voise
@bot.message_handler(content_types=['text', 'document', 'audio'])
def mmm(message):
    num_voise = message.text.split()[-1]
    if message.text == 'Поздороваться':
        bot.send_message(message.from_user.id, 'ну привет')
    elif message.text == 'картинка':
        file = open('23.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text == 'Прибавь звук':
        bot.send_message(message.chat.id, 'прибавил звук')
        soundup10(20)
    elif message.text == "Убавь звук":
        bot.send_message(message.chat.id, 'убавил звук')
        sounddown10()
    elif message.text == f"Убавь звук на {num_voise}":
        bot.send_message(message.chat.id, 'убавил звук')
        sounddown10(int(num_voise))
    elif message.text == f'Прибавь звук на {num_voise}':
        bot.send_message(message.chat.id, 'прибавил звук')
        soundup10(int(num_voise))
    else:
        bot.send_message(message.from_user.id, 'я не знаю чего ты хочешь')

bot.infinity_polling()

# if __name__ == '__main__':
#     statrt()
