#Установите модуль ephem
#Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, 
# например /planet Mars
#В функции-обработчике команды из update.message.text получите название планеты 
# (подсказка: используйте .split())
#При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня
# находится планета.

import ephem
import logging
import setting
from emoji import emojize
from glob import glob
from random import choice, randint
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

logging.basicConfig(filename = 'bot.log',level = logging.INFO)

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

def greet_user(update,context):
    print('Вызван /start') # написать в консоле
    #print(update) # информация о пользователе 
    context.user_data['emoji'] = get_smile(context.user_data)#обьявление того что мы хотим использовать нужые смайлики
    update.message.reply_text(f"Здравствуй,пользователь! {context.user_data['emoji']}") #написать пользователю

def talk_to_me(update,context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text},{context.user_data['emoji']}")

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(setting.USER_EMOJI)
        return emojize(smile,use_aliases=True)
    return user_data['emoji'] # аналогия с else


def play_random_numbers (user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число  {user_number}, мое число {bot_number}, вы выиграли'
    elif user_number == bot_number:
         message = f'Ваше число  {user_number}, мое число {bot_number}, ничья'
    else:
         message = f'Ваше число  {user_number}, мое число {bot_number}, проиграл'
    return message


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
    update.message.reply_text(message)
def send_cat_picture(update,context):
    cat_photo_list = glob('images/cat*.jp*g')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id #ид чата
    context.bot.send_photo(chat_id= chat_id,photo=open(cat_photo_filename,'rb'))
#открываем контекст бот отправить фото в чат ид фото открыть (рандомное фот ов бинарном формате)
def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(setting.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet',planet_user))
    dp.add_handler(CommandHandler('quess',guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   
    logging.info('Бот стартовал')

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
if __name__ == '__main__':
    main()
    #проврка моей теории о неверности ссылки на гит