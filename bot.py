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
    update.message.reply_text('Здравствуй,пользователь!') #написать пользователю

def talk_to_me(update,context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(setting.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet',planet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   
    logging.info('Бот стартовал')

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
if __name__ == '__main__':
    main()