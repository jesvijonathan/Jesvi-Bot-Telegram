from modules import *
from modules.core import *
from config import *

from telegram import Message, Chat, Update, Bot, User, ChatMember
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram.utils.helpers import escape_markdown


import logging

from mysql import connector

import time

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import threading
print("imoprting modules")

# Bot Logging & Debugging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
print("logging")

# Bot Authentication
updater = Updater(bot_token, use_context=True)
dp = updater.dispatcher
print("authenticating")

# Initialize Database & Cursor
def load():
    db = connector.connect(
    host=database_host,
    user=database_user,
    password=database_password)
    cursor = db.cursor(buffered=True)

    sql = "CREATE DATABASE IF NOT EXISTS {s0}".format(s0=database_name)
    cursor.execute(sql)

    db = connector.connect(
    host=database_host,
    user=database_user,
    password=database_password,
    database=database_name)
    cursor = db.cursor(buffered=True)
    
    database_create = database.database_create(cursor, db)
    database_create.create_base()

load()
print("database loaded")

def unparse(update, context):  # Unparse Incoming Responses
    start = time.process_time()

    msg = update.message
    # print("\n", msg)

    user = msg['from_user']
    chat = msg['chat']

    tag_user = None

    try:
        tagmsg = update.message.reply_to_message

        tag_user = tagmsg['from_user']

        database.add_user(user=tag_user)

    except:
        pass

    database.add_user(user=user)
    database.add_chat(chat=chat)
    database.add_link(chat=chat, user=user)

    # user_status = context.bot.get_chat_member(chat['id'], user['id'])
    # print(user_status['status'])

    # print(chatmember)
    # print(eval(str(context.bot.getChat(chat['id']).permissions)))

    print("\n", time.process_time() - start, "\n")


def button(update: Update, context: CallbackContext):
    start = time.process_time()
    
    query = update.callback_query
    func = query.data.split(' ', 1)[0]
    
    # print("\n", query.message.reply_markup, "\n")
    # print("\n", query.message.reply_to_message.from_user, "\n")
    # print("\n", query.data, "\n")
    # print("\n", query.from_user, "\n")
    # query.answer(text='you chose dog!', show_alert=True)
    # full_msg = query.message.reply_to_message

    if func == "veri":
        but_veri(update,context) # try with later **locals()

    print("\n", time.process_time() - start, "\n")


def but_veri(update: Update, context: CallbackContext):
    query = update.callback_query

    user = query.from_user
    # print(user)
    user_id = user.id

    # print("\n", msg.new_chat_members[0].id)
    # print(msg.from_user.id)
    # print(user_id, "\n")
    data = query.data.split(' ', 2)
    msg = query.message.reply_to_message

    if user_id == msg.new_chat_members[0].id:
        chat = msg.chat
        chat_id = chat.id

        query.answer()

        #text = query.data[2]

        query.edit_message_text(text=data[2])

        if data[1] == '0':
            mute.unmute(context, chat_id=chat_id,
                        user_id=user_id)
            database.add_link(chat=chat, user=user, replace=1)

        # user_status = context.bot.get_chat_member(chat_id, user_id)
        # print(user_status['status'])

    else:
        query.answer(
                text='You are already verified, This button is not for you !')


def main():  # Main Function
    print("started")

    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome.gate))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(Filters.all, unparse))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
