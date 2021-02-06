
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hello(update, context):
    update.message.reply_text('Assalom aleykum botga hush kelipsiz')


updater = Updater(
    '1623452611:AAHhPixDjQH2sre-onqGwwrBaamPZ5Uvips', use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.start_polling()
updater.idle()