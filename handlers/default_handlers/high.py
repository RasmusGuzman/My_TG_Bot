from keyboards.inline import inline_keyboard
from telebot.types import Message
from config_data.config import RAPID_API_KEY
from loader import bot
import requests



@bot.message_handler(commands=['high'])
def bot_high(message: Message):
    chat_id = message.chat.id
    incl_kb = inline_keyboard.search_keyboard_high()
    bot.reply_to(message, f"Выберите категорию, в которой надо произвести сортировку по дате(max)", reply_markup=incl_kb)
    @bot.callback_query_handler(func=lambda call: call.data == '2.1')
    def rev_actors_list(call):
        url = "https://moviesdatabase.p.rapidapi.com/actors"
        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        rev_actors_dict = response.json()
        rev_sorted_list = {}

        for i_elem in rev_actors_dict['results']:
            rev_sorted_list[i_elem["primaryName"]] = i_elem["birthYear"]
        rev_sorted_scores = sorted(rev_sorted_list.items(), key=lambda x: x[1], reverse=True)
        bot.send_message(chat_id, 'Cколько актеров из списка показать?', reply_markup=inline_keyboard.len_keyboard_1())

        @bot.callback_query_handler(func=lambda call: call.data == '1.5')
        def print_half_list(call):
            text = [f"{actors} родился в {year} году" for actors, year in rev_sorted_scores[:5]]
            bot.send_message(chat_id, "\n".join(text))

        @bot.callback_query_handler(func=lambda call: call.data == '1.все')
        def print_list(call):
            text = [f"{actors} родился в {year} году" for actors, year in rev_sorted_scores]
            bot.send_message(chat_id, "\n".join(text))

    @bot.callback_query_handler(func=lambda call: call.data == '2.2')
    def  rev_films_list(call):
        url = "https://moviesdatabase.p.rapidapi.com/titles"

        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        rev_films_dict = response.json()
        rev_movey_list = {}

        for i_elem in rev_films_dict['results']:
            rev_movey_list[i_elem["titleText"]["text"]] = i_elem["releaseYear"]["year"]
        rev_sorted_movey = sorted(rev_movey_list.items(), key=lambda x: x[1], reverse=True)
        bot.send_message(chat_id, 'Cколько фильмов из списка показать?', reply_markup=inline_keyboard.len_keyboard_2())

        @bot.callback_query_handler(func=lambda call: call.data == '2.5')
        def print_half_list(call):
            text = [f"{film} появился в {year} году" for film, year in rev_sorted_movey[:5]]
            bot.send_message(chat_id, "\n".join(text))

        @bot.callback_query_handler(func=lambda call: call.data == '2.все')
        def print_half_list(call):
            text = [f"{film} появился в {year} году" for film, year in rev_sorted_movey]
            bot.send_message(chat_id, "\n".join(text))
