import logging
import requests

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,)



CHOICE, RATIONAL_ONE, RATIONAL, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(8)

API_URL = 'https://7015.deeppavlov.ai/model'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, _):
    reply_keyboard = [['Операции с рациональными числами', 'Операции с комплесными числами', 'Cancel']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в калькулятор.', reply_markup=markup_key)
    return CHOICE


def choice(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice == 'Операции с рациональными числами':
        update.message.reply_text(
            'Введите первое рациональное число')

        return RATIONAL_ONE

    if user_choice == 'Операции с комплесными числами':
        context.bot.send_message(
            update.effective_chat.id, 'Введите Re и Im первого числа через ПРОБЕЛ: ')
        return COMPLEX_ONE
    if user_choice == 'Cancel':
        return cancel(update, context)


def rational_one(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_one'] = get_rational
        update.message.reply_text(
            'Введите второе рациональное')
        return RATIONAL_TWO

    else:
        update.message.reply_text(
            'Нужно ввести число')


def rational(update, context):
    data = {'x': [update.message.text]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    print(res[0][0])
    print(res)
    update.message.reply_text(res[0][0])
    return start(update, context)


def rational_two(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_two'] = get_rational
        reply_keyboard = [['+', '-', '*', '/']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
        'Выберите операцию с числами', reply_markup=markup_key)
        return OPERATIONS_RATIONAL


def operatons_rational(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    rational_one = context.user_data.get('rational_one')
    rational_two = context.user_data.get('rational_two')
    user_choice = update.message.text
    if user_choice == '+':
        result = rational_one + rational_two
    if user_choice == '-':
        result = rational_one - rational_two
    if user_choice == '*':
        result = rational_one * rational_two
    if user_choice == '/':
        try:
            result = rational_one / rational_two
        except:
            update.message.reply_text('Деление на ноль запрещено')
    update.message.reply_text(
        f'Результат: {rational_one} + {rational_two} = {result}')
    return start(update, context)


def complex_one(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь ввел число %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_one = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_one'] = complex_one
        update.message.reply_text(
            f'Первое число {complex_one},  Введите Re и Im второго числа через ПРОБЕЛ: ')
        return COMPLEX_TWO
    else:
        update.message.reply_text('Это не то. Введите Re и Im первого числа через ПРОБЕЛ')


def complex_two(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь ввел число %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_two = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_two'] = complex_two
        update.message.reply_text(f'Второе число {complex_two}')
        reply_keyboard = [['+', '-', '*', '/']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
        'Выберите операцию с числами', reply_markup=markup_key)
        return OPERATIONS_COMPLEX
    else:
        update.message.reply_text('Это не то. Введите Re и Im второго числа через ПРОБЕЛ')

def operatons_complex(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    complex_one = context.user_data.get('complex_one')
    complex_two = context.user_data.get('complex_two')
    user_choice = update.message.text
    if user_choice == '+':
        result = complex_one + complex_two
    if user_choice == '-':
        result = complex_one - complex_two
    if user_choice == '*':
        result = complex_one * complex_two
    if user_choice == '/':
        try:
            result = complex_one / complex_two
        except:
            update.message.reply_text('Деление на ноль запрещено')
    update.message.reply_text(
        f'Результат: {complex_one} + {complex_two} = {result}')
    return start(update, context)

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться.\n'
        ' Захочешь посчитать - заходи.',
    )
    return ConversationHandler.END