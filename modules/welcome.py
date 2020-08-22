
import sys 
sys.path.append('./')

import config as config


def greet(update, context):
    for new_member in update.message.new_chat_members:
            if str(new_member['id']) == str(config.bot_id):
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