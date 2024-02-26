from telebot.types import Message
from loader import bot
from keyboards.reply import reply_keyboard
from config_data.config import DEFAULT_COMMANDS

@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!👋", reply_markup=reply_keyboard.reply_kb())
    bot.send_message(message.chat.id,'Меня зовут VR-Bro, и я твой пресональный проводник в удивительный мир кино! Я пока только учусь, но уже умею это👇')
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))