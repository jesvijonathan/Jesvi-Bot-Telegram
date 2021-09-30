
#from modules import *
#from modules.core import *
from config import *


import modules.core.database as database
import modules.core.mute as mute
import modules.core.welcome as welcome
#import  modules.core.extract as extract

import  modules.core.filter as filter

import  modules.core.unparse as unparse

import modules.delete as delete

import modules.core.note as note


from telegram import Message, Chat, Update, Bot, User, ChatMember
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram.utils.helpers import escape_markdown

import logging

from mysql import connector

import time

import sys
import os

import threading

"""
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import threading"""

print("imoprted modules")


# Bot Logging & Debugging
platform = sys.platform

path = path = str(os.path.dirname(os.path.dirname(sys.argv[0])))
stdoutOrigin = sys.stdout

deb = 1 # switch to 1 when debugging, to prevent log file creation

if platform == "linux" or platform == "linux2" or platform == "darwin":
    sys.stderr = open(path+"/../logs/log_bot_runtime.log", 'w')

elif platform == "win32":
    wp= path + '\\logs\\log_bot_runtime.log'
    filename = os.path.join(wp)
    
    if deb == 0:
        logging.basicConfig(filename=filename,
                        filemode='a',
                        format='%(asctime)s %(levelname)s %(name)s %(message)s',
                        level=logging.DEBUG)
        #sys.stdout = open(wp, 'w')
        sys.stderr = open(wp, 'w')
    else:
        logging.basicConfig(
                        format='%(asctime)s %(levelname)s %(name)s %(message)s',
                        level=logging.DEBUG)
        logger = logging.getLogger(__name__)
                        
class writer(object):
    log = []

    def write(self, data):
        self.log.append(data)

print("logging")


# Bot Authentication
print("authenticating")
updater = Updater(bot_token, use_context=True)
dp = updater.dispatcher


# Initialize Database & Cursor
botdb = None

def load():
    global botdb
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
    
    create_db = database.create_db().create_base()
    #del create_db

    botdb = database.bot_db()

load()
print("database loaded")


def unparse_func(update, context):  # Unparse Incoming Responses
    start = time.process_time()
    
    msg = update.message

    user = msg['from_user']
    chat = msg['chat']

    tag_user = None

    try:
        tagmsg = update.message.reply_to_message

        tag_user = tagmsg['from_user']

        botdb.add_user(user=tag_user)

    except:
        pass

    botdb.parse(chat=chat, user=user)

    # user_status = context.bot.get_chat_member(chat['id'], user['id'])
    # print(user_status['status'])
    # print(chatmember)
    # print(eval(str(context.bot.getChat(chat['id']).permissions)))
    
    threading.Thread(target=filter.filter, args=(msg,chat,user,tag_user), daemon=True).start()

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

    if deb == 0:
        logger = writer()
        sys.stdout = logger
        sys.stderr = logger
    
    dp.bot.send_message(chat_id=owner_id, text="<code>Started Service !\n\nTime : " +
                        time.strftime("%Y-%m-%d (%H:%M:%S)") + "</code>", parse_mode="HTML")


    delete_cmd = ("delete", "remove")


    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome.gate))
    dp.add_handler(MessageHandler(
        Filters.status_update.left_chat_member, welcome.farewell))


    dp.add_handler(CommandHandler("delete", delete.tag_del_cls)) # delete.tag_del_cls
    dp.add_handler(CommandHandler("purge", delete.mul_del_cls))
    dp.add_handler(CommandHandler("sdel", delete.s_del_cls))

    #dp.add_handler(CommandHandler("admin", delete.lock))
    dp.add_handler(CommandHandler("lock", filter.filter_router))
    dp.add_handler(CommandHandler("unlock", filter.filter_router))

    dp.add_handler(CommandHandler("filter", filter.filter_router))
    dp.add_handler(CommandHandler("filteradd", filter.filter_router))
    dp.add_handler(CommandHandler("filterdel", filter.filter_router))

    
    dp.add_handler(CommandHandler("noteadd", note.note_router))
    dp.add_handler(CommandHandler("notedel", note.note_router))
    dp.add_handler(CommandHandler("notes", note.note_router))
    
    #dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(Filters.all, unparse_func))
    #dp.add_handler(MessageHandler(Filters.all, unparse.thread_unparse))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

#new stuff for sub-main 2