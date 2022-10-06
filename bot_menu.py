import telebot
import os

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start, help'])
def star_command(message):
    bot.send_message(message.chat.id, "Тут я расскажу что умею")


@bot.message_handler(commands=['restart'])
def shutdown_command(message):
    bot.send_message(message.chat.id, "Перезагрузка копьютера")
    os.system('shutdown /r')


@bot.message_handler(commands=['shutdown'])
def shutdown_command(message):
    bot.send_message(message.chat.id, "Выключение копьютера")
    os.system('shutdown /s')


@bot.message_handler(commands=['sleep'])
def lock_command(message):
    bot.send_message(message.chat.id, "Спящий режим")
    os.system('shutdown /h')


bot.polling(none_stop=True, interval=0)
