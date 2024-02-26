from telebot import types
def start_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    Help = types.InlineKeyboardButton(text="Помощь", callback_data='/help')
    Low = types.InlineKeyboardButton(text="Cортировка(мин)", callback_data="/low")
    High = types.InlineKeyboardButton(text="Cортировка(макс)", callback_data="/high")
    Custom = types.InlineKeyboardButton(text="Cписок данных", callback_data="/custom")
    History = types.InlineKeyboardButton(text="История запросов", callback_data="/history")
    keyboard.add(Help, Low, High, Custom, History)
    return keyboard


def search_keyboard_low():
    keyboard = types.InlineKeyboardMarkup()
    Actors = types.InlineKeyboardButton(text="Актеры", callback_data='low1')
    Films = types.InlineKeyboardButton(text="Фильмы", callback_data='low2')
    keyboard.add(Actors, Films)
    return keyboard

def len_keyboard_low1():
    keyboard = types.InlineKeyboardMarkup()
    Five = types.InlineKeyboardButton(text="Первые 5", callback_data='6')
    All = types.InlineKeyboardButton(text="Весь список", callback_data='all')
    keyboard.add(Five, All)
    return keyboard

def len_keyboard_low2():
    keyboard = types.InlineKeyboardMarkup()
    Five = types.InlineKeyboardButton(text="Первые 5", callback_data='6.1')
    All = types.InlineKeyboardButton(text="Весь список", callback_data='all.1')
    keyboard.add(Five, All)
    return keyboard

def search_keyboard_high():
    keyboard = types.InlineKeyboardMarkup()
    Actors = types.InlineKeyboardButton(text="Актеры", callback_data='2.1')
    Films = types.InlineKeyboardButton(text="Фильмы", callback_data='2.2')
    keyboard.add(Actors, Films)
    return keyboard

def len_keyboard_1():
    keyboard = types.InlineKeyboardMarkup()
    Five = types.InlineKeyboardButton(text="Первые 5", callback_data='1.5')
    All = types.InlineKeyboardButton(text="Весь список", callback_data='1.все')
    keyboard.add(Five, All)
    return keyboard

def len_keyboard_2():
    keyboard = types.InlineKeyboardMarkup()
    Five = types.InlineKeyboardButton(text="Первые 5", callback_data='2.5')
    All = types.InlineKeyboardButton(text="Весь список", callback_data='2.все')
    keyboard.add(Five, All)
    return keyboard

def custom_search_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    actors = types.InlineKeyboardButton(text="Актеры", callback_data='custom_1')
    films = types.InlineKeyboardButton(text="Фильмы", callback_data='custom_2')
    keyboard.add(actors, films)
    return keyboard
