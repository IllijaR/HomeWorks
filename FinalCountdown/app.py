import telebot
from telebot import types
from MyRegestration import LogDataBase

API_TOKEN = 'secret :)'
bot = telebot.TeleBot(API_TOKEN)
db = LogDataBase()


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Войти', 'Зарегистрироваться')
    msg = bot.reply_to(message, "Войти или зарегистрироваться?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_choice)


@bot.message_handler(func=lambda message: True)
def choice(message):
    start(message)


def process_choice(message):
    if message.text == 'Войти':
        msg = bot.reply_to(message, "Введи логин:")
        bot.register_next_step_handler(msg, login)
    elif message.text == 'Зарегистрироваться':
        msg = bot.reply_to(message, "Введи логин:")
        bot.register_next_step_handler(msg, registration_login)


def login(message):
    user_login = message.text
    msg = bot.reply_to(message, "Введи пароль:")
    bot.register_next_step_handler(msg, login_password, user_login)


def login_password(message, user_login):
    user_password = message.text
    if db.login_user(user_login, user_password):
        bot.reply_to(message, "Успешный вход!")
    else:
        bot.reply_to(message, "Что-то введено неверно.")


def registration_login(message):
    user_login = message.text
    if db.check_login(user_login):
        msg = bot.reply_to(message, "Введите Емайл:")
        bot.register_next_step_handler(msg, registration_email, user_login)
    else:
        bot.reply_to(message, "Неправильный формат логина.")


def registration_email(message, user_login):
    user_email = message.text
    if db.check_email(user_email):
        msg = bot.reply_to(message, "Введите пароль:")
        bot.register_next_step_handler(msg, registration_password, user_login, user_email)
    else:
        bot.reply_to(message, "Почта неверная.")


def registration_password(message, user_login, user_email):
    user_password = message.text
    if db.check_password(user_password):
        if db.register_or_update_user(user_login, user_email, user_password):
            bot.reply_to(message, "Регестрация успешна!")
        else:
            bot.reply_to(message, "Ошибка.")
    else:
        bot.reply_to(message,
                     "Слабый пароль или с @.")


if __name__ == '__main__':
    bot.polling()
