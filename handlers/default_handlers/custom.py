from keyboards.inline import inline_keyboard
from telebot.types import Message
from config_data.config import RAPID_API_KEY
from loader import bot
import requests
from keyboards.reply import reply_keyboard

@bot.message_handler(commands=['custom'])
def bot_custom(message: Message):
    global chat_id
    chat_id = message.chat.id
    custom_kb = inline_keyboard.custom_search_keyboard()
    bot.reply_to(message, f"Выберите категорию, в которой надо произвести поиск", reply_markup=custom_kb)
    @bot.callback_query_handler(func=lambda call: call.data == 'custom_1')
    def check_data_act(call):
        global user_value
        user_value = 'custom_1'
        bot.send_message(chat_id, 'Введите мин. кол-во букв, которые должны быть в моем ответе:')
        bot.register_next_step_handler(message, check_start_num)

    @bot.callback_query_handler(func=lambda call: call.data == 'custom_2')
    def check_data_films(call):
        global user_value
        user_value = 'custom_2'
        bot.send_message(chat_id, 'Введи мин. кол-во букв, которые должны быть в моем ответе:')
        bot.register_next_step_handler(message, check_start_num)
def check_start_num(message):
    global start_num
    start_num = None
    try:
        start_num = int(message.text)  # проверяем корректность введеных данных
    except Exception:
        bot.send_message(chat_id, 'Ты должен указать любое целое число для того, чтобы я обработал твой запрос!')
        bot.send_message(chat_id, 'Введи мин. кол-во букв, которые должны быть в моем ответе:')
        bot.register_next_step_handler(message, check_start_num)
    if start_num:
        bot.send_message(chat_id, 'Отлично! Теперь введи макс. кол-во букв, которые должны быть в моем ответе:')
        bot.register_next_step_handler(message, check_final_num)


def check_final_num(message):
    global user_value
    global final_num
    final_num = None
    try:
        final_num = int(message.text)
    except Exception:
        bot.send_message(chat_id, 'Ты должен указать любое целое число для того, чтобы я обработал товй запрос!')
        bot.send_message(chat_id, 'Введи макс. кол-во букв, которые должны быть в моем ответе:')
        bot.register_next_step_handler(message, check_final_num)
    if final_num:
        if start_num >= final_num:
            bot.send_message(chat_id, 'Макс. число букв не может быть меньше или равно мин. числу букв!')
            bot.send_message(chat_id, 'Введи макс. кол-во букв, которые должны быть в моем ответе:')
            bot.register_next_step_handler(message, check_final_num)
        else:
            bot.send_message(chat_id, 'Ты готов получить готовый список?', reply_markup=reply_keyboard.reply_custom())
            if user_value == 'custom_1':
                bot.register_next_step_handler(message, rev_actors_list)
            elif user_value == 'custom_2':
                bot.register_next_step_handler(message, rev_films_list)


def rev_actors_list(message):
    url = "https://moviesdatabase.p.rapidapi.com/actors"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    custom_dict = response.json()
    custom_list = []

    for i_elem in custom_dict['results']:
        custom_list.append([i_elem["primaryName"]])

    sorted_custom_list = [x[0] for x in custom_list if start_num <= len(x[0]) <= final_num]
    if len(sorted_custom_list) > 0:
        text = [f"{index + 1}: {actors} " for index, actors in enumerate(sorted_custom_list)]
        bot.send_message(chat_id, "\n".join(text), reply_markup=reply_keyboard.reply_kb())
    else:
        bot.send_message(chat_id, 'К сожалению, я не нашел актеров с указанными параметрами🤷🏻‍♂️', reply_markup=reply_keyboard.reply_kb())


def rev_films_list(message):
    url = "https://moviesdatabase.p.rapidapi.com/titles"

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    custom_films_dict = response.json()
    custom_films = []

    for i_elem in custom_films_dict['results']:
        custom_films.append([i_elem["titleText"]["text"]])

    sorted_custom_films = [x[0] for x in custom_films if start_num <= len(x[0]) <= final_num]
    if len(sorted_custom_films) > 0:
        text = [f"{index + 1}: {actors} " for index, actors in enumerate(sorted_custom_films)]
        bot.send_message(chat_id, "\n".join(text), reply_markup=reply_keyboard.reply_kb())
    else:
        bot.send_message(chat_id, 'К сожалению, я не нашел фильмов с указанными параметрами🤷🏻‍♂️', reply_markup=reply_keyboard.reply_kb())

