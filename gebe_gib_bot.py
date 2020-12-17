#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger("GEBE_GIB_BOT")

def utostr(user):
    if user.username: 
        return str(user.id) + ":" + user.username
    else:
        return str(user.id)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Bittet, dann wird euch gegeben.')
    logger.info(utostr(update.effective_user) + " hat sich registriert")


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/gib und dir wird gegeben\n/gebe und dir wird gegeben.')
    logger.info("Hilfe angezeigt fuer " + utostr(update.effective_user))

def log_message(bot, update):
    """Echo the user message."""
    logger.info(utostr(update.effective_user) + " schrieb: " + update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def gib(bot, update): 
    update.message.reply_text("nimm!")
    logger.info(utostr(update.effective_user) + " hat genommen")


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("770515348:AAFG5vNsPXMKIgDs-xhrgjOR0OypoDYr2c4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("gib", gib))
    dp.add_handler(CommandHandler("gebe", gib))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, log_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
