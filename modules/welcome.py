
import sys 
sys.path.append('./')

import config as config
import database as database
import re
import modules.info as info
from modules.edit import rules

def dat(update, context,sync=0):
    chat = update.effective_chat
    count = update.effective_chat.get_members_count()

    chat_id = chat['id']
    bot_activity = context.bot.get_chat_member(chat_id, config.bot_id)

    chat_id = re.sub(r'[^\w]', '', str(chat_id))

    database.create_base()

    if sync == 0:
        msg = update.message.reply_text("Syncing..")
        database.add_chat_base(chat_id,chat['username'],chat['title'],bot_activity['status'],count,sync=sync)
        msg.edit_text("Current Chat Base Updated !")
    else:
        database.add_chat_base(chat_id,chat['username'],chat['title'],bot_activity['status'],count,sync=sync)


def ldat(update,context):
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id
    
    user = context.bot.get_chat_member(chat_id, user_id)

    chat_id = re.sub(r'[^\w]', '', str(chat_id))

    database.add_link_base(chat_id=chat_id,user_id=str(user_id),status=user['status'])
    

def udat(update, context,sync=0):
    user = update.message.from_user

    database.create_base()

    database.add_user_base(user_id=str(user['id']),firstname=user['first_name'],username=user['username'],lastname=user['last_name'],is_bot=user['is_bot'])

    chat = update.effective_chat.type
    if chat != "private":
        dat(update,context,1)
        ldat(update,context)

         

def start_func(update,context):
    if update.effective_chat.type != 'private':
        update.message.reply_text(text = "<a href='http://t.me/jesvi_bot?start=start'>"+ "Click Here" +"</a>" + " to get started !", parse_mode="HTML",disable_web_page_preview=True)
        return

    res = update.message.text.split(None, 2)
    
    try:
        t = res[0] + res[1]
        if res[1] == "help":
            return
        elif res[1] == "start":
            pass
        else:
            rules(update,context)
            return
    except:
        pass

    about(update,context)
    udat(update,context)


def greet(update, context):

    for new_member in update.message.new_chat_members:
            if str(new_member['id']) == str(config.bot_id):
                dat(update,context,1)
                ldat(update,context)
                welcome_text = "Hello !\n\n" + "This is Jesvi Bot & I am a telegram handler bot developed by my owner @jesvijonathan,\n\nUse /help, /about or PM me @jesvi_bot for more info 😁 "
            else:
                group = update.message["chat"]
                user = new_member
                database.add_user_base(user_id=str(user['id']),firstname=user['first_name'],username=user['username'],lastname=user['last_name'],is_bot=user['is_bot'])

                welcome_text = "Welcome to " + str(group['title']) + ", "+ str(new_member['first_name']) + " ! 🥳"
    
    update.message.reply_text(text=welcome_text, 
                  parse_mode="HTML")


def farewell(update, context):
    user = left_member = update.effective_message.left_chat_member
    database.add_user_base(user_id=str(user['id']),firstname=user['first_name'],username=user['username'],lastname=user['last_name'],is_bot=['is_bot'])
                
    farewell_text = "Bye " + str(left_member['first_name']) + ", 👋🏼"
    update.effective_message.reply_text(farewell_text)


def owner(update,conetxt):
    text = ("I am still being built by my owner @jesvijonathan & am being tested in @bot_garage for proper functionality &" +
            "\nFYI : you CAN NOT PM him without a good reason or be ready to get banned\nHave a nice day ! ;)")
    update.message.reply_text(text)


def about(update,conetxt):
    text = "This is Jesvi Bot & I am a telegram handler bot being developed by my owner @jesvijonathan.\nfor any further disccussion, join @bot_garage to have a lil chat with my maintainer :)"
    update.message.reply_text(text)
