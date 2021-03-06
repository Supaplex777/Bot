from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup,KeyboardButton #клавиатура
import setting


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

def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать котика', KeyboardButton('Мои координаты',request_location=True)]])