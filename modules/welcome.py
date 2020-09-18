
import sys 
sys.path.append('./')

import config as config
import database as database
import re
import modules.info as info

def dat(update, context,sync=0):
    chat_id = update.effective_chat.id
    bot_activity = context.bot.get_chat_member(chat_id, config.bot_id)
    chat_id = re.sub(r'[^\w]', '', str(chat_id))
    group_name = update.effective_chat.title
    username = update.effective_chat.username
    count = update.effective_chat.get_members_count()

    database.create_base()

    if sync == 0:
        msg = update.message.reply_text("Syncing..")
        database.add_chat_base(chat_id,username,group_name,bot_activity['status'],count,sync)
        msg.edit_text("Current Chat Base Updated !")
    else:
        database.add_chat_base(chat_id,username,group_name,bot_activity['status'],count,sync)


def greet(update, context):

    for new_member in update.message.new_chat_members:
            if str(new_member['id']) == str(config.bot_id):
                dat(update,context,1)
                welcome_text = "Hello !\n\n" + "This is Jesvi Bot & I am a telegram handler bot developed by my owner @jesvijonathan,\n\nUse /help, /about or PM me @jesvi_bot for more info 😁 "
            else:
                group = update.message["chat"]
                welcome_text = "Welcome to " + str(group['title']) + ", "+ str(new_member['first_name']) + " ! 🥳"
    
    update.message.reply_text(text=welcome_text, 
                  parse_mode="HTML")


def farewell(update, context):
    left_member = update.effective_message.left_chat_member
    farewell_text = "Bye " + str(left_member['first_name']) + ", 👋🏼"
    update.effective_message.reply_text(farewell_text)