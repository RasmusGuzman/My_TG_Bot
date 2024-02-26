from keyboards.inline import inline_keyboard
from telebot.types import Message
from config_data.config import RAPID_API_KEY
from loader import bot
import requests



@bot.message_handler(commands=['low'])
def bot_low(message: Message):
    chat_id = message.chat.id
    incl_fb = inline_keyboard.search_keyboard_low()
    bot.reply_to(message, f"Выберите категорию, в которой надо произвести сортировку по дате(min)", reply_markup=incl_fb)
    @bot.callback_query_handler(func=lambda call: call.data == 'low1')
    def actors_list(call):
        url = "https://moviesdatabase.p.rapidapi.com/actors"
        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        actors_dict = response.json()
        sorted_list = {}

        for i_elem in actors_dict['results']:
            sorted_list[i_elem["primaryName"]] = i_elem["birthYear"]
        sorted_scores = sorted(sorted_list.items(), key=lambda x: x[1])
        bot.send_message(chat_id, 'Cколько актеров из списка показать?', reply_markup=inline_keyboard.len_keyboard_low1())

        @bot.callback_query_handler(func=lambda call: call.data == '6')
        def print_half_list(call):
            text = [f"{actors} родился в {year} году" for actors, year in sorted_scores[:5]]
            bot.send_message(chat_id, "\n".join(text))

        @bot.callback_query_handler(func=lambda call: call.data == 'all')
        def print_half_list(call):
            text = [f"{actors} родился в {year} году" for actors, year in sorted_scores]
            bot.send_message(chat_id, "\n".join(text))

    @bot.callback_query_handler(func=lambda call: call.data == 'low2')
    def  films_list(call):
        url = "https://moviesdatabase.p.rapidapi.com/titles"

        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        films_dict = response.json()
        movey_list = {}

        for i_elem in films_dict['results']:
            movey_list[i_elem["titleText"]["text"]] = i_elem["releaseYear"]["year"]
        sorted_movey = sorted(movey_list.items(), key=lambda x: x[1])
        bot.send_message(chat_id, 'Cколько фильмов из списка показать?', reply_markup=inline_keyboard.len_keyboard_low2())

        @bot.callback_query_handler(func=lambda call: call.data == '6.1')
        def print_half_list(call):
            text = [f"{film} появился в {year} году" for film, year in sorted_movey[:5]]
            bot.send_message(chat_id, "\n".join(text))

        @bot.callback_query_handler(func=lambda call: call.data == 'all.1')
        def print_half_list(call):
            text = [f"{film} появился в {year} году" for film, year in sorted_movey]
            bot.send_message(chat_id, "\n".join(text))
