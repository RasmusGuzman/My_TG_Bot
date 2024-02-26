from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['history'])
def bot_start(message: Message):
    bot.reply_to(message, f"Извини, {message.from_user.full_name}, но мой создатель еще не разработал этот раздел😔")