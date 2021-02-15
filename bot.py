import logging
import setting
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

logging.basicConfig(filename = 'bot.log',level = logging.INFO)
def greet_user(update,context):
    print('Вызван /start') # написать в консоле
    print(update) # информация о пользователе 
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
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
if __name__ == '__main__':
    main()