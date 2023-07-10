import telebot


bot = telebot.TeleBot('5868508351:AAHDjQ1D9uYfxhckwCgJwEBgoq4q3dk3Exw')



@bot.message_handler(content_types=['text', 'document', 'audio'])
def statrt(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'ну привет')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")



bot.polling(none_stop=True,interval=0)


if __name__ == '__main__':
    statrt()
