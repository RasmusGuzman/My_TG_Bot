from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def reply_kb():
    my_rp_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    low = KeyboardButton(text='/low')
    high = KeyboardButton(text='/️high')
    custom = KeyboardButton(text='/custom')
    history = KeyboardButton(text='/history')
    my_rp_kb.add(low, high, custom, history)
    return my_rp_kb

def reply_custom():
    cust_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_but = KeyboardButton(text='🙋🏻‍♂️Да')
    cust_kb.add(yes_but)
    return cust_kb

