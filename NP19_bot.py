from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, datetime

import ephem
import logging

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

methods = {'mercury': ephem.Mercury, 'venus': ephem.Venus, 'mars': ephem.Mars, 'jupiter': ephem.Jupiter, 'saturn': ephem.Saturn, 'uranus': ephem.Uranus, 'neptune': ephem.Neptune, 'pluto': ephem.Pluto}

def main():
    mybot = Updater ("869248774:AAHJFrBOmMfQB0ZNkZ5pm-KPTZlqmumBQa8", request_kwargs=PROXY )

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    dp.add_handler(CommandHandler("planet", say_constellation ))

    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
       text = 'Вызван /start'
       print(text)
       update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def say_constellation(bot, update):
    user_text = update.message.text.split()
    planet = user_text[1]
    dt = datetime.now().strftime('%Y/%m/%d')
    if planet in methods:
        planet_today = methods[planet](dt)
        update.message.reply_text(ephem.constellation(planet_today))
    else:
        update.message.reply_text('Нет такой планеты')


main()