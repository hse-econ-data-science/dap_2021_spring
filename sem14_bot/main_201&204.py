import telebot
from telebot import types
import requests

token = "1859580468:AAGAHg0nTZC9vY9arYL9ENXNJnuyShzo2HE"

bot = telebot.TeleBot(token)

# напишем, что делать нашему боту при команде старт
@bot.message_handler(commands=['start'])
def send_keyboard(message, text="Привет, чем я могу тебе помочь?"):
    
    keyboard = types.ReplyKeyboardMarkup(row_width=1)  # наша клавиатура
    itembtn1 = types.KeyboardButton('Сделать красиво') # создадим кнопку
    itembtn2 = types.KeyboardButton('Пока все!')
    keyboard.add(itembtn1, itembtn2) 

    # пришлем это все сообщением и запишем выбранный вариант
    msg = bot.send_message(message.from_user.id,
                     text=text, reply_markup=keyboard)

    # отправим этот вариант в функцию, которая его обработает
    bot.register_next_step_handler(msg, callback_worker)
    

def get_infa(num):
    url = f"https://api.isevenapi.xyz/api/iseven/{num}"
    res = requests.get(url)
    infa = res.json()
    return infa['ad'], infa['iseven']


def send_number(msg):
    try:
        ad, res = get_infa(msg.text)
    except:
        ad, res = 'error', 'error'
        
    bot.send_message(msg.chat.id, ad)
    bot.send_message(msg.chat.id, res)
    bot.send_message(msg.chat.id, 'Покупай премиум: https://isevenapi.xyz/')
    
    send_keyboard(msg, "Чем еще могу помочь?")

# привязываем функции к кнопкам на клавиатуре
def callback_worker(call):
    
    if call.text == 'Сделать красиво':
        msg = bot.send_message(call.chat.id, 'Напиши число между 0 и 999 999 в чат.')
        bot.register_next_step_handler(msg, send_number)


    elif call.text == "Пока все!":
        bot.send_message(call.chat.id, 'Хорошего дня! Когда захотите продолжнить нажмите на команду /start')
        
        
@bot.message_handler(content_types=['text'])
def handle_docs_audio(message):
    send_keyboard(message, text="Я не понимаю :-( Выберите один из пунктов меню:")
        
    
bot.polling(none_stop=True)

