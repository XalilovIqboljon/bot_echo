import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hello(update, context):
    update.message.reply_text('Assalom aleykum botga hush kelipsiz')

token = os.environ['token_echo']
updater = Updater(
    token, use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.start_polling()
updater.idle()