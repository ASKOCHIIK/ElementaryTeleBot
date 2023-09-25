import telebot
from telebot import types

bot = telebot.TeleBot('6314055634:AAE56tJPZBjALeQ7w939FcRFY4_8F_ZUDxM')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Саламчик, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Салам':
        bot.send_message(message.chat.id, "Сагада салам !")
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Сенин IDин: {message.from_user.id}")
    elif message.text == 'Музыка':
        audio = open('НаZима - Я Твоя.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Фото':
        photo = open('IMG_0749.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Видео':
        video = open('video_1_4cb92cdc367e4ad19883fa61c7c02cb2.MOV', 'rb')
        bot.send_video_note(message.chat.id, video)
    else:
        bot.send_message(message.chat.id, "Мен сени тушуно албай жатам!")


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Баззар жок! Жакшы фото экен.')


@bot.message_handler(commands=['Сайт'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Бат жазганды уйронгун келсе!', url='https://typerun.top/#eng_basic'))
    bot.send_message(message.chat.id, 'Бул жакты бас', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    pass


bot.polling(none_stop=True)
