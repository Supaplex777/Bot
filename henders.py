import ephem
from glob import glob
from random import choice
from utils import get_smile, play_random_numbers, main_keyboard






def greet_user(update,context):
    print('Вызван /start') # написать в консоле
    #print(update) # информация о пользователе 
    context.user_data['emoji'] = get_smile(context.user_data)#обьявление того что мы хотим использовать нужые смайлики
    update.message.reply_text(
        f"Здравствуй,пользователь! {context.user_data['emoji']}",
        reply_markup= main_keyboard()) #написать пользователю


def talk_to_me(update,context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text},{context.user_data['emoji']}", reply_markup= main_keyboard()) 

def guess_number(update,context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0]) # от нуля 
            message = play_random_numbers(user_number)
        except (TypeError,ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введи число'
    update.message.reply_text(message,reply_markup= main_keyboard()) 

def send_cat_picture(update,context):
    cat_photo_list = glob('images/cat*.jp*g')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id #ид чата
    context.bot.send_photo(chat_id= chat_id,photo=open(cat_photo_filename,'rb'),reply_markup= main_keyboard()) 
#открываем контекст бот отправить фото в чат ид фото открыть (рандомное фот ов бинарном формате)

def user_coordinates (update,context): #координаты
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(f"Ваши координаты: {coords} {context.user_data['emoji']}!",reply_markup=main_keyboard())

def planet_user (update,context):
    print('Вызван /planet')
    message =  update.message.text.split()[1]
    print(message)

    if message =='Venus':
        update.message.reply_text(ephem.constellation(ephem.Venus('2021/01/01')))
    elif message == 'Mars':
        update.message.reply_text(ephem.constellation(ephem.Mars('2021/01/01')))
    elif message == 'Mercury':
         update.message.reply_text(ephem.constellation(ephem.Mercury('2021/01/01')))
    elif message == 'Jupiter':
        update.message.reply_text(ephem.constellation(ephem.Jupiter('2021/01/01')))
    elif message == 'Saturn':
         update.message.reply_text(ephem.constellation(ephem.Saturn('2021/01/01')))
    elif message == 'Uranus':
         update.message.reply_text(ephem.constellation(ephem.Uranus('2021/01/01')))
    elif message == 'Neptune':
         update.message.reply_text(ephem.constellation(ephem.Neptune('2021/01/01')))
    elif message == 'Pluto':
         update.message.reply_text(ephem.constellation(ephem.Pluto('2021/01/01')))
    else:
        update.message.reply_text('Напиши планеты солнечной системы')
