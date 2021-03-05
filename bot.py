#Установите модуль ephem
#Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, 
# например /planet Mars
#В функции-обработчике команды из update.message.text получите название планеты 
# (подсказка: используйте .split())
#При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня
# находится планета.

import logging
import setting
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from henders import greet_user,guess_number,send_cat_picture,user_coordinates,talk_to_me,planet_user

logging.basicConfig(filename = 'bot.log',level = logging.INFO)


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(setting.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet',planet_user))
    dp.add_handler(CommandHandler('quess',guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'),send_cat_picture)) #регулярные выражения 
    dp.add_handler(MessageHandler(Filters.location,user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

   
    logging.info('Бот стартовал')

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
if __name__ == '__main__':
    main()
    #проврка моей теории о неверности ссылки на гит