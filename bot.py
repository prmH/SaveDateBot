import telebot
import config

username = ''

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['hi'])
def send_hi_message(message):
    print(message.from_user.id)
    bot.send_message(message.from_user.id, 'Hi! Как тебя зовут?')
    bot.register_next_step_handler(message, save_name)


def save_name(message):
    global username
    username = message.text
    bot.send_message(message.from_user.id, 'Hi, {0}!'.format(username))


bot.polling(none_stop=True, interval=0)
