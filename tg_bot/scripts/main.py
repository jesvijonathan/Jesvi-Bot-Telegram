
#from modules import *
#from modules.core import *

try:
    from config1 import *
except:
    from config import *


import modules.core.database as database

import modules.core.welcome as welcome
#import  modules.core.extract as extract

import  modules.core.filter as filter

import  modules.core.unparse as unparse

import modules.delete as delete

import modules.core.note as note

import modules.core.rule as rule

import modules.core.warn as warn

import modules.core.ban as ban

import modules.core.edit as edit


import modules.core.extract as extract

import modules.core.fun as fun
import modules.core.help as help

import modules.core.system as system

import modules.core.database as bot_db

import modules.core.fun as fun

import modules.extras as extras

from telegram import Message, Chat, Update, Bot, User, ChatMember, bot
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

deb = 0 # switch to 1 when debugging, to prevent log file creation

if platform == "linux" or platform == "linux2" or platform == "darwin":
    sys.stderr = open(path+"/logs/log_bot_runtime.log", 'w')

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


    # user_status = context.bot.get_chat_member(chat['id'], user['id'])
    # print(user_status['status'])
    # print(chatmember)
    # print(eval(str(context.bot.getChat(chat['id']).permissions)))
    
    threading.Thread(target=unparse.filter, args=(update,context), daemon=True).start()

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
            ban.ban_cls(update,context).unmute()
            database.add_link(chat=chat, user=user, replace=1)

        # user_status = context.bot.get_chat_member(chat_id, user_id)
        # print(user_status['status'])

    else:
        query.answer(
                text='You are already verified, This button is not for you !')


def start(update,context):
    res = update.message.text.split(None,1)

    try:
        sub = res[1]
        if sub == "start":
            text = "This is " + bot_name + " & I am a telegram handler bot being developed with @jesvi_bot 's source code to provide users with a better UX experience... \n\nAdd me in a group and you can get started to use my features.\n\n" +\
           "You can check out for my source/feature updates at @bot_garage_channel\n\nUse /help for more info about available commands & its uses.."
            update.message.reply_text(text)
        
        elif sub == "help":
            help.help(update,context)
        elif sub == "rules":
            rule.rule_router(update,context)
        elif sub == "set":
            pass
        elif sub == "note":
            pass
        elif sub.startswith('-') == True:
            rule.rule_router(update,context)
    except:    
        text = "This is " + bot_name + " & I am a telegram handler bot being developed with @jesvi_bot 's source code to provide users with a better UX experience... \n\nAdd me in a group and you can get started to use my features.\n\n" +\
           "You can check out for my source/feature updates at @bot_garage_channel\n\nUse /help for more info about available commands & its uses.."
        update.message.reply_text(text)

def rel(update, context):
    #text = "<a href='tg://user?id=" + str(user_id) + "'>" + first_name + "</a>" +\
    #                ", you have been muted... \n\nClick on the human verification button within the next 2min to unmute yourself !"   # else, you will be kicked !"
    """
    url1 = "https://github.com/jesvijonathan/Jesvi-Bot-Telegram"
    url2 = "https://telegram.me/bot_garage_channel"

    keyboard = [
        [
            InlineKeyboardButton(text="", callback_data='1', url=url1),
         ],
         [
             InlineKeyboardButton(text="", callback_data='2', url=url2)
         ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    """

    res = update.message.text.split(None,1)

    try:
        text = res[1]
        uid = res[0]
    except Exception as x:
        update.message.reply_text(x)
        return


    """
    cha = botdb.get_chat()
        
    for x,y in enumerate(cha):
        try:
            context.bot.send_message(chat_id=y[0], text=text, reply_markup=reply_markup, parse_mode="HTML", disable_web_page_preview=True)
        except:
            pass
    """

    context.bot.send_message(chat_id=uid, text=text,parse_mode="HTML", disable_web_page_preview=True)
        

def main():  # Main Function
    print("started")
    uptime = str(time.strftime("%Y-%m-%d (%H:%M:%S)"))

    if deb == 0:
        logger = writer()
        sys.stdout = logger
        sys.stderr = logger
    
    dp.bot.send_message(chat_id=owner_id, text="<code>Started Service !\n\nTime : " +
                        uptime + "</code>", parse_mode="HTML")

    dp.add_handler(CommandHandler("rel", rel))

    start_cmd = ("start", "about")
    dp.add_handler(CommandHandler(start_cmd, start))

    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome.gate))
    dp.add_handler(MessageHandler(
        Filters.status_update.left_chat_member, welcome.farewell))

    delete_cmd = ("del", "purge", "sdel")
    dp.add_handler(CommandHandler(delete_cmd, delete.delete_router))

    filter_cmd = ("lock", "unlock", "filter", "filteradd", "filterdel")
    dp.add_handler(CommandHandler(filter_cmd, filter.filter_router))

    notes_cmd = ("notes", "noteadd", "notedel")
    dp.add_handler(CommandHandler(notes_cmd, note.note_router))

    warn_cmd = ("warn", "warninfo", "warnclear", "warnremove")
    dp.add_handler(CommandHandler(warn_cmd, warn.warn_router))

    ban_cmd = ("ban", "unban", "kick", "mute", "unmute","leave", "rip")
    dp.add_handler(CommandHandler(ban_cmd, ban.thread_ban))

    rule_cmd = ("rules", "rule","ruleset", "ruledel")
    dp.add_handler(CommandHandler(rule_cmd, rule.rule_router))


    extras_cmd = ("search")
    dp.add_handler(CommandHandler(extras_cmd, extras.extras_threading))

    system_cmd = ("net", "sql", "system", "cmd", "server", "publish")
    dp.add_handler(CommandHandler(system_cmd, system.system_threading))

    
    dp.add_handler(CommandHandler("scoot", quit_))
    
    fun_cmd = ("boom")
    dp.add_handler(CommandHandler(fun_cmd, fun.boom))
    fun_cmd = ("oof")
    dp.add_handler(CommandHandler(fun_cmd, fun.oof))
    fun_cmd = ("fbi")
    dp.add_handler(CommandHandler(fun_cmd, fun.fbi_joke))

    help_cmd = ("help")
    dp.add_handler(CommandHandler(help_cmd, help.help))

    edit_cmd = ("promote", "demote", "pin", "unpin", "bio", "bioset", "biodel", "descset", "nickset", "titleset")
    dp.add_handler(CommandHandler(edit_cmd, edit.edit_router))

    info_cmd = ("info", "group", "msgid", "json", "sync")
    dp.add_handler(CommandHandler(info_cmd, unparse.thread_unparse))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(Filters.all, unparse_func))
    #dp.add_handler(MessageHandler(Filters.all, unparse.thread_unparse))
    
    updater.start_polling()
    updater.idle()
    

def quit_(update,context):
    m = extract.sudo_check_2(msg=update.message,del_lvl=7,context=context,sudo=1)
    if m== 7:
        pass
    else: return

    context.bot.send_message(chat_id=update.message['chat']["id"],text="Terminating !" ,
                                parse_mode="HTML")

    updater.stop()
    exit(1)
    system.exit(1)
    return


if __name__ == '__main__':
    main()

#new stuff for sub-main 2