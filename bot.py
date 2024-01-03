import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! постарайтесь соблюдать эти правила,\
    что-бы тебя опубликовали:\n1. Присылайте несколько фоток, если одна фотка есть \
    шанс что вас не опубликуют\n2. Тебе должно быть от 18 лет\n3. Желательно краткое\
    описание на 1-2 предложения\n4. За спам и оск баним в чате\nСтараемся публиковать\
    все быстро, и по очереди, поэтому извините если задержка с вашей анкетой\n@TeloPodpischicy')


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, 'Привет! постарайтесь соблюдать эти правила,\
    что-бы тебя опубликовали:\n1. Присылайте несколько фоток, если одна фотка есть \
    шанс что вас не опубликуют\n2. Тебе должно быть от 18 лет\n3. Желательно краткое\
    описание на 1-2 предложения\n4. За спам и оск баним в чате\nСтараемся публиковать\
    все быстро, и по очереди, поэтому извините если задержка с вашей анкетой\n@TeloPodpischicy')


 

@bot.message_handler(content_types=["photo"])
def photo(message):
    thanks = bot.send_message(message.chat.id, '@' + message.chat.username + ' Теперь надо немножко подождать и мы все запостим😘😘😘')
    user = bot.send_message(config.owner, '@' + message.chat.username)
    bot.forward_message(config.owner, message.chat.id, message.message_id, user, thanks)



@bot.message_handler(content_types=["voice"])
def voice(message):
    thanks = bot.send_message(message.chat.id, '@' + message.chat.username + ' Теперь надо немножко подождать и мы все запостим, но лучше скинь нам фоточки или видео🥰🥰🥰')
    user = bot.send_message(config.owner, '@' + message.chat.username)
    bot.forward_message(config.owner, message.chat.id, message.message_id, user, thanks)


@bot.message_handler(content_types=["video_note"])
def video_note(message):
    thanks = bot.send_message(message.chat.id, '@' + message.chat.username + ' Теперь надо немножко подождать и мы все запостим, но если тут ничего интересного мы обидемся😘😘😘')
    user = bot.send_message(config.owner, '@' + message.chat.username)
    bot.forward_message(config.owner, message.chat.id, message.message_id, user, thanks)


@bot.message_handler(content_types=["sticker"])
def sticker(message):
    user = bot.send_message(config.owner, '@' + message.chat.username)
    bot.forward_message(config.owner, message.chat.id, message.message_id, user)


@bot.message_handler(content_types=["video"])
def video(message):
    thanks = bot.send_message(message.chat.id, '@' + message.chat.username + ' Теперь надо немножко подождать и мы все запостим😘😘😘')
    user = bot.send_message(config.owner, '@' + message.chat.username)
    bot.forward_message(config.owner, message.chat.id, message.message_id, user, thanks)


@bot.message_handler(content_types=["animation"])
def animation(message):
    thanks = bot.send_message(message.chat.id, '@' + message.chat.username + ' Теперь надо немножко подождать и мы все запостим😘😘😘')
    user = bot.send_message(config.owner, '@' + message.chat.username)
    bot.forward_message(config.owner, message.chat.id, message.message_id, user, thanks)


@bot.message_handler(content_types=["text"])
def messages(message):
    bot.send_message(config.owner, str('@' + message.chat.username) + ': ' + message.text)
    bot.reply_to_message(message.chat.id, '@' + message.chat.username + ' Лучше скинь нам фоточки или видео🥰🥰🥰')



if __name__ == '__main__':
    bot.polling(none_stop=True)