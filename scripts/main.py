from modules import *
from modules.database import *
from config import *

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

import logging

from mysql import connector


# Bot Logging & Debugging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


# Bot Authentication
updater = Updater(bot_token, use_context=True)
dp = updater.dispatcher


# Initialize Database & Cursor
mydb = connector.connect(
    host=database_host,
    user=database_user,
    password=database_password,
    database=database_name)
mycursor = mydb.cursor(prepared=True)


def unparse(update, context):  # Unparse Incoming Responses
    msg = update.message
    # print(msg, "\n")
    tagmsg = update.message.reply_to_message
    # print(tagmsg, "\n")

    chat = msg['chat']
    user = msg['from_user']
    print("\nchat : ", chat)
    print("\nfrm_usr : ", user)

    #create.user_base(mycursor=mycursor, mydb=mydb)
    #create.chat_base(mycursor=mycursor, mydb=mydb)

    add.user(mycursor=mycursor, mydb=mydb, user=user)
    add.chat(mycursor=mycursor, mydb=mydb, chat=chat)


def main():  # Main Function
    print("started")
    dp.add_handler(MessageHandler(Filters.all, unparse))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
