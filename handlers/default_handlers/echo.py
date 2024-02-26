from telebot.types import Message
from loader import bot
from config_data.config import DEFAULT_COMMANDS

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю твоего сообщения. Нажми на одну из кнопок выше или перейди в одно из этих меню👇:\n /help для получения помощи\n/start для того, чтобы перезапустить бота")
