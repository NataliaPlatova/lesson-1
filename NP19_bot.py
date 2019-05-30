from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem
import logging

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater ("869248774:AAHJFrBOmMfQB0ZNkZ5pm-KPTZlqmumBQa8", request_kwargs=PROXY )

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # dp.add_handler(CommandHandler("planet", "planet_name", say_constellation ))

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

#def say_constellation(bot, update):
 #   user_text = update.message.text.split()
  #  if ephem.constellation
   #     update.message.reply_text(ephem.constellation(user_text))

main()